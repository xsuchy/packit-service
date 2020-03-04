"""store build timestamp

Revision ID: 509652e21254
Revises: 258490f6e667
Create Date: 2020-03-04 07:29:52.618091

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "509652e21254"
down_revision = "258490f6e667"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "copr_builds", sa.Column("build_finished_time", sa.Integer(), nullable=True)
    )
    op.add_column(
        "copr_builds", sa.Column("build_start_time", sa.Integer(), nullable=True)
    )
    op.add_column(
        "copr_builds", sa.Column("build_submitted_time", sa.Integer(), nullable=True)
    )
    op.drop_column("copr_builds", "logs")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "copr_builds", sa.Column("logs", sa.TEXT(), autoincrement=False, nullable=True)
    )
    op.drop_column("copr_builds", "build_submitted_time")
    op.drop_column("copr_builds", "build_start_time")
    op.drop_column("copr_builds", "build_finished_time")
    # ### end Alembic commands ###
