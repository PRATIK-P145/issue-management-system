"""baseline schema

Revision ID: c1048a693357
Revises: 30ebfde58db6
Create Date: 2026-01-11 17:01:33.299078

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c1048a693357'
down_revision: Union[str, Sequence[str], None] = '30ebfde58db6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
