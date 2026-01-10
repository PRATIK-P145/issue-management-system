"""add created_at and priority to issues

Revision ID: d8ec92204e2d
Revises: 5b33ce88e990
Create Date: 2026-01-10 18:05:13.402885

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd8ec92204e2d'
down_revision: Union[str, Sequence[str], None] = '5b33ce88e990'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column(
        'issues',
        sa.Column(
            'created_at',
            sa.DateTime(),
            server_default=sa.func.now(),
            nullable=False
        )
    )

    op.add_column(
        'issues',
        sa.Column(
            'priority',
            sa.String(length=20),
            nullable=True
        )
    )

def downgrade():
    op.drop_column('issues', 'priority')
    op.drop_column('issues', 'created_at')
