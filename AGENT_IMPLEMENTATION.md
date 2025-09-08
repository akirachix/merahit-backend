# Agent Management Implementation Guide

## Question: "Why do we need this AgentViewSet?"

This document addresses the question about the necessity of implementing an `AgentViewSet` in the Django REST API.

## Summary

**AgentViewSet is likely NOT needed** because the existing `UsersViewSet` can handle agent management efficiently through filtering and custom actions.

## Implementation Options

### Option 1: Use Existing UsersViewSet (Recommended)

**Advantages:**
- ✅ Follows existing patterns
- ✅ Reduces code duplication
- ✅ Maintains consistency
- ✅ Less maintenance overhead

**API Endpoints:**
```bash
# List all agents
GET /api/users/?usertype=agent

# Create an agent
POST /api/signup/
{
    "full_name": "Agent Name",
    "phone_number": "1234567890",
    "password": "password",
    "usertype": "agent",
    "department": "Sales"
}

# Get specific agent
GET /api/users/{id}/

# Update agent
PUT /api/users/{id}/

# Delete agent
DELETE /api/users/{id}/

# Custom action: List agents
GET /api/users/list_agents/
```

### Option 2: Dedicated AgentViewSet (Optional)

Only implement this if agents need special functionality that `UsersViewSet` doesn't provide.

**When to use:**
- Agents have complex business logic
- Need agent-specific endpoints
- Different permissions for agent operations
- Special filtering/sorting requirements

**API Endpoints:**
```bash
# If you uncomment the router registration in urls.py:
GET /api/agents/                    # List all agents
POST /api/agents/                   # Create agent
GET /api/agents/{id}/               # Get specific agent
PUT /api/agents/{id}/               # Update agent
DELETE /api/agents/{id}/            # Delete agent
GET /api/agents/list_agents/        # Custom action (redundant)
GET /api/agents/agents_by_department/?department=Sales  # Agent-specific feature
```

## Code Changes Made

### 1. Added Agent User Type
```python
# users/models.py
USER_TYPE_CHOICES = (
    ('customer', 'Customer'),
    ('mamamboga', 'Mama Mboga'),
    ('admin', 'Admin'),
    ('agent', 'Agent'),  # ← Added this
)
```

### 2. Created Agent Model
```python
# users/models.py
class Agent(Users):
    agent_id = models.CharField(max_length=50, unique=True, null=True, blank=True)
    department = models.CharField(max_length=100, default='General')
    hire_date = models.DateField(auto_now_add=True)
    # ... (automatically sets usertype='agent')
```

### 3. Added AgentSerializer
```python
# api/serializers.py
class AgentSerializer(serializers.ModelSerializer):
    # Specialized serializer for agent-specific fields
```

### 4. Enhanced UsersViewSet
```python
# api/views.py
class UsersViewSet(viewsets.ModelViewSet):
    # ... existing code ...
    
    @action(detail=False, methods=['get'], url_path='list_agents')
    def list_agents(self, request):
        """Custom action to list all agents."""
        agents = Users.objects.filter(usertype='agent')
        serializer = self.get_serializer(agents, many=True)
        return Response(serializer.data)
```

### 5. Implemented Optional AgentViewSet
```python
# api/views.py
class AgentViewSet(viewsets.ModelViewSet):
    """Optional - only use if special agent functionality is needed."""
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    # ... with agent-specific actions
```

## Usage Examples

### Creating an Agent
```python
# Method 1: Using existing signup endpoint
POST /api/signup/
{
    "full_name": "John Doe",
    "phone_number": "1234567890",
    "password": "securepass",
    "usertype": "agent",
    "department": "Sales"
}

# Method 2: Using admin interface or direct API
# (if AgentViewSet is enabled)
POST /api/agents/
{
    "full_name": "Jane Smith",
    "phone_number": "0987654321",
    "password": "securepass",
    "department": "Support"
}
```

### Retrieving Agents
```python
# Method 1: Filter users by type (Recommended)
GET /api/users/?usertype=agent

# Method 2: Custom action
GET /api/users/list_agents/

# Method 3: If AgentViewSet is enabled
GET /api/agents/
```

## Testing

Run the agent management tests:
```bash
python manage.py test api.test_agent_management
```

## Recommendation

**Use Option 1 (UsersViewSet with filtering)** unless you have specific requirements that justify implementing a separate AgentViewSet.

The existing architecture is designed to handle multiple user types efficiently, and adding a separate ViewSet for each user type would lead to code duplication and increased maintenance overhead.

## Migration

If you decide to implement this, create and run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

## Enabling AgentViewSet

If you decide you need the dedicated AgentViewSet, uncomment this line in `api/urls.py`:
```python
# router.register(r"agents", AgentViewSet, basename="agent")
```