# Generated by Django 3.2.18 on 2023-04-23 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField()),
                ('approach', models.IntegerField()),
                ('automatic_accept_date', models.DateTimeField()),
                ('automatic_accept_email', models.CharField(blank=True, max_length=100, null=True)),
                ('closing_date', models.DateTimeField()),
                ('closing_email', models.CharField(blank=True, max_length=100, null=True)),
                ('competence', models.IntegerField()),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('group_legend', models.IntegerField()),
                ('month_challenge_forecast', models.IntegerField()),
                ('opening_date', models.DateTimeField()),
                ('projection_indicator_id', models.BigIntegerField(blank=True, null=True)),
                ('status_budget', models.IntegerField()),
                ('type_budget', models.IntegerField()),
                ('type_projection', models.IntegerField()),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='companies.company')),
            ],
            options={
                'db_table': 'budget',
            },
        ),
        migrations.CreateModel(
            name='CompetenceCostCenterStructure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('competence', models.IntegerField()),
            ],
            options={
                'db_table': 'competencecostcenterstructure',
            },
        ),
        migrations.CreateModel(
            name='CostCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='cost_centers', to='budgets.budget')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='cost_centers', to='companies.company')),
            ],
            options={
                'db_table': 'costcenter',
            },
        ),
        migrations.CreateModel(
            name='CostClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField()),
                ('budget', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='cost_classes', to='budgets.budget')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='cost_classes', to='companies.company')),
            ],
            options={
                'db_table': 'costclass',
            },
        ),
        migrations.CreateModel(
            name='ParametrizationCostClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('use', models.IntegerField()),
                ('cost_class_code', models.CharField(blank=True, max_length=100, null=True)),
                ('group_cost_class_code', models.CharField(blank=True, max_length=100, null=True)),
                ('module', models.IntegerField()),
            ],
            options={
                'db_table': 'parametrizationcostclass',
            },
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_permission', models.IntegerField()),
                ('user_network', models.CharField(blank=True, max_length=100, null=True)),
                ('budget', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='permissions', to='budgets.budget')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='permissions', to='companies.company')),
                ('cost_center', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='permissions', to='budgets.costcenter')),
                ('cost_class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='permissions', to='budgets.costclass')),
            ],
            options={
                'db_table': 'permission',
            },
        ),
        migrations.CreateModel(
            name='Itemfilter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='item_filters', to='budgets.budget')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='item_filters', to='companies.company')),
                ('cost_center', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='item_filters', to='budgets.costcenter')),
                ('filter', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='item_filters', to='companies.filter')),
            ],
            options={
                'db_table': 'itemfilter',
            },
        ),
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('competence', models.IntegerField()),
                ('type_indicator', models.IntegerField()),
                ('percentual', models.IntegerField()),
                ('month', models.IntegerField()),
                ('type_readjustment', models.IntegerField()),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='indicators', to='companies.company')),
            ],
            options={
                'db_table': 'indicator',
            },
        ),
        migrations.CreateModel(
            name='CostClassStructure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('type_cost_class', models.IntegerField()),
                ('is_package', models.BooleanField()),
                ('purpose', models.IntegerField()),
                ('pmso', models.IntegerField()),
                ('is_blocked_projection', models.BooleanField()),
                ('is_blocked_base_scenario', models.BooleanField()),
                ('is_blocked_free_account', models.BooleanField()),
                ('is_blocked_activation', models.BooleanField()),
                ('is_blocked_shared', models.BooleanField()),
                ('competence', models.IntegerField()),
                ('is_negative_value', models.BooleanField()),
                ('indicator_classification', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='cost_structure_classifications', to='budgets.indicator')),
                ('indicator_material_service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='cost_structures_material_services', to='budgets.indicator')),
                ('indicator_projection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='cost_structure_projections', to='budgets.indicator')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='cost_structures', to='budgets.costclassstructure')),
            ],
            options={
                'db_table': 'costclassstructure',
            },
        ),
        migrations.AddField(
            model_name='costclass',
            name='cost_class_structure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='cost_classes', to='budgets.costclassstructure'),
        ),
        migrations.CreateModel(
            name='CostCenterStructure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=100, null=True)),
                ('coverage_code', models.IntegerField()),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('type_cost_center', models.IntegerField()),
                ('coverage', models.IntegerField()),
                ('hierarchy', models.IntegerField(blank=True, null=True)),
                ('deadline_release', models.DateTimeField()),
                ('competence', models.IntegerField()),
                ('activatable', models.BooleanField()),
                ('shared', models.BooleanField()),
                ('competence_cost_center_structure', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='cost_center_structures', to='budgets.competencecostcenterstructure')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='cost_center_structures', to='budgets.costcenterstructure')),
            ],
            options={
                'db_table': 'costcenterstructure',
            },
        ),
        migrations.AddField(
            model_name='costcenter',
            name='cost_center_structure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='cost_centers', to='budgets.costcenterstructure'),
        ),
        migrations.AddField(
            model_name='budget',
            name='indicator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='budgets', to='budgets.indicator'),
        ),
    ]
