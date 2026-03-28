# ---! Repository Package
# ---! Bu dosya tüm repository sınıflarını dışa aktarır

from ._base_repository import BaseRepository
from ._repository_abc import RepositoryABC

# ---! Application Schema Models (Dosyalar oluşturulduğunda açılacak)
# from .application_repository import (
#     ApplicationRepository,
# )

# from .team_repository import (
#     TeamRepository,
# )

# from .employee_repository import (
#     EmployeeRepository,
# )

# from .department_repository import (
#     DepartmentRepository,
# )

# from .role_repository import (
#     RoleRepository,
# )

# from .manager_repository import (
#     ManagerRepository,
# )

# ---! Tüm repository'leri dışa aktarma listesi
__all__ = [
    "BaseRepository",
    "RepositoryABC",
    # "ApplicationRepository",
    # "TeamRepository",
    # "EmployeeRepository",
    # "DepartmentRepository",
    # "RoleRepository",
    # "ManagerRepository",
]
