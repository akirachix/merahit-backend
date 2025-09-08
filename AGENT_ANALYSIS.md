# AgentViewSet Analysis and Implementation

## Question: "Why do we need this AgentViewSet?"

The question refers to this code snippet:
```python
class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    @action(detail=False, methods=['get'], url_path='list_agents')
```

## Analysis

After analyzing the codebase, **this AgentViewSet is likely NOT needed** for the following reasons:

### 1. No Agent Model Exists
- There is no `Agent` model defined in the codebase
- There is no `AgentSerializer` defined
- The existing models are: Users, Customer, MamaMboga, Product, Order, etc.

### 2. Existing User Management System
The current system already supports different user types through the `Users` model:
- **customer**: Regular customers
- **mamamboga**: Vendors/sellers
- **admin**: Administrative users

### 3. UsersViewSet Already Handles User Types
The existing `UsersViewSet` provides:
```python
class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['usertype']  # ← Already supports filtering by user type!
    permission_classes = [IsAdminOrSelf]
```

## Alternative Solutions

### Option 1: Use Existing UsersViewSet (Recommended)
If agents are just another user type, you can:

1. **Add 'agent' to USER_TYPE_CHOICES:**
```python
USER_TYPE_CHOICES = (
    ('customer', 'Customer'),
    ('mamamboga', 'Mama Mboga'),
    ('admin', 'Admin'),
    ('agent', 'Agent'),  # ← Add this
)
```

2. **Filter agents using existing endpoint:**
```
GET /api/users/?usertype=agent
```

3. **Create agents using existing signup:**
```json
POST /api/signup/
{
    "full_name": "Agent Name",
    "phone_number": "1234567890",
    "password": "password",
    "usertype": "agent"
}
```

### Option 2: Implement AgentViewSet (If Special Functionality Needed)
Only implement AgentViewSet if agents need functionality that UsersViewSet doesn't provide.

## Recommendation

**DO NOT implement AgentViewSet** unless agents require special functionality beyond what the existing UsersViewSet provides. The current system is already designed to handle multiple user types efficiently.

If you need to list agents specifically, use:
```
GET /api/users/?usertype=agent
```

This approach:
- ✅ Follows existing patterns
- ✅ Reduces code duplication
- ✅ Maintains consistency
- ✅ Is more maintainable