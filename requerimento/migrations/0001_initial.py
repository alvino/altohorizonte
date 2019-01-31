# Generated by Django 2.0.5 on 2019-01-29 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='assinante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('cargo', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Assinatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assinante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requerimento.assinante')),
            ],
        ),
        migrations.CreateModel(
            name='AtaRegistoPreco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contrato', models.CharField(max_length=10)),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CentroCusto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razao', models.CharField(max_length=150)),
                ('cnpj', models.CharField(max_length=14)),
                ('telefone', models.CharField(max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='ItemRequerido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('unidade', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ItemRequeridoARP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.DecimalField(decimal_places=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='ProdutoARP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=12)),
                ('arp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requerimento.AtaRegistoPreco')),
                ('fornercedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requerimento.Fornecedor')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requerimento.Produto')),
            ],
        ),
        migrations.CreateModel(
            name='Requerimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('justificativa', models.TextField()),
                ('destino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requerimento.CentroCusto')),
            ],
        ),
        migrations.CreateModel(
            name='RequerimentoARP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('justificativa', models.TextField()),
                ('destino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requerimento.CentroCusto')),
            ],
        ),
        migrations.CreateModel(
            name='Secretaria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='requerimentoarp',
            name='origem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requerimento.Secretaria'),
        ),
        migrations.AddField(
            model_name='requerimento',
            name='origem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requerimento.Secretaria'),
        ),
        migrations.AddField(
            model_name='itemrequeridoarp',
            name='produtoARP',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requerimento.ProdutoARP'),
        ),
        migrations.AddField(
            model_name='itemrequeridoarp',
            name='requerimentoARP',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requerimento.RequerimentoARP'),
        ),
        migrations.AddField(
            model_name='itemrequerido',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requerimento.Produto'),
        ),
        migrations.AddField(
            model_name='itemrequerido',
            name='requerimento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requerimento.Requerimento'),
        ),
        migrations.AddField(
            model_name='assinatura',
            name='requerimento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requerimento.Requerimento'),
        ),
    ]
