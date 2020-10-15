# Generated by Django 3.1.1 on 2020-10-15 11:07

from django.db import migrations


def create_temporary_channel(apps, schema_editor):
    # TODO: REMOVE ME BEFORE MERGE TO MASTER
    # This migration is needed for test deployments
    Channel = apps.get_model("channel", "Channel")

    Channel.objects.create(
        name="Other Channel USD",
        slug="other-usd-channel",
        currency_code="USD",
        is_active=True,
    )


class Migration(migrations.Migration):

    dependencies = [
        ("channel", "0002_channel_availability"),
        ("product", "0134_auto_20201006_0635"),
        ("discount", "0023_voucherchannellisting"),
        ("order", "0090_orderchannel"),
        ("checkout", "0031_auto_20200819_0912"),
        ("shipping", "0022_auto_20200910_1000"),
    ]

    operations = [
        migrations.RunPython(create_temporary_channel, migrations.RunPython.noop),
    ]
