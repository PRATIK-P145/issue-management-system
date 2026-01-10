"""backfill and enforce priority

Revision ID: c036647c9e35
Revises: 392d3dd784af
Create Date: 2026-01-10 19:51:17.802085

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c036647c9e35'
down_revision: Union[str, Sequence[str], None] = '392d3dd784af'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # 1. Backfill existing NULL values
    op.execute(
        "UPDATE issues SET priority = 'medium' WHERE priority IS NULL"
    )

    # 2. Set server default
    op.alter_column(
        'issues',
        'priority',
        server_default='medium'
    )

    # 3. Enforce NOT NULL
    op.alter_column(
        'issues',
        'priority',
        nullable=False
    )


def downgrade():
    op.alter_column(
        'issues',
        'priority',
        nullable=True
    )

    op.alter_column(
        'issues',
        'priority',
        server_default=None
    )