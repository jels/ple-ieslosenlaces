#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file has been automatically generated, changes may be lost if you
# go and generate it again. It was generated with the following command:
# manage.py dumpscript

import datetime
from decimal import Decimal
from django.contrib.contenttypes.models import ContentType

def run():
    from django.contrib.auth.models import Permission

    auth_permission_1 = Permission()
    auth_permission_1.name = u'Can add log entry'
    auth_permission_1.content_type = ContentType.objects.get(app_label="admin", model="logentry")
    auth_permission_1.codename = u'add_logentry'
    auth_permission_1.save()

    auth_permission_2 = Permission()
    auth_permission_2.name = u'Can change log entry'
    auth_permission_2.content_type = ContentType.objects.get(app_label="admin", model="logentry")
    auth_permission_2.codename = u'change_logentry'
    auth_permission_2.save()

    auth_permission_3 = Permission()
    auth_permission_3.name = u'Can delete log entry'
    auth_permission_3.content_type = ContentType.objects.get(app_label="admin", model="logentry")
    auth_permission_3.codename = u'delete_logentry'
    auth_permission_3.save()

    auth_permission_4 = Permission()
    auth_permission_4.name = u'Can add group'
    auth_permission_4.content_type = ContentType.objects.get(app_label="auth", model="group")
    auth_permission_4.codename = u'add_group'
    auth_permission_4.save()

    auth_permission_5 = Permission()
    auth_permission_5.name = u'Can add message'
    auth_permission_5.content_type = ContentType.objects.get(app_label="auth", model="message")
    auth_permission_5.codename = u'add_message'
    auth_permission_5.save()

    auth_permission_6 = Permission()
    auth_permission_6.name = u'Can add permission'
    auth_permission_6.content_type = ContentType.objects.get(app_label="auth", model="permission")
    auth_permission_6.codename = u'add_permission'
    auth_permission_6.save()

    auth_permission_7 = Permission()
    auth_permission_7.name = u'Can add user'
    auth_permission_7.content_type = ContentType.objects.get(app_label="auth", model="user")
    auth_permission_7.codename = u'add_user'
    auth_permission_7.save()

    auth_permission_8 = Permission()
    auth_permission_8.name = u'Can change group'
    auth_permission_8.content_type = ContentType.objects.get(app_label="auth", model="group")
    auth_permission_8.codename = u'change_group'
    auth_permission_8.save()

    auth_permission_9 = Permission()
    auth_permission_9.name = u'Can change message'
    auth_permission_9.content_type = ContentType.objects.get(app_label="auth", model="message")
    auth_permission_9.codename = u'change_message'
    auth_permission_9.save()

    auth_permission_10 = Permission()
    auth_permission_10.name = u'Can change permission'
    auth_permission_10.content_type = ContentType.objects.get(app_label="auth", model="permission")
    auth_permission_10.codename = u'change_permission'
    auth_permission_10.save()

    auth_permission_11 = Permission()
    auth_permission_11.name = u'Can change user'
    auth_permission_11.content_type = ContentType.objects.get(app_label="auth", model="user")
    auth_permission_11.codename = u'change_user'
    auth_permission_11.save()

    auth_permission_12 = Permission()
    auth_permission_12.name = u'Can delete group'
    auth_permission_12.content_type = ContentType.objects.get(app_label="auth", model="group")
    auth_permission_12.codename = u'delete_group'
    auth_permission_12.save()

    auth_permission_13 = Permission()
    auth_permission_13.name = u'Can delete message'
    auth_permission_13.content_type = ContentType.objects.get(app_label="auth", model="message")
    auth_permission_13.codename = u'delete_message'
    auth_permission_13.save()

    auth_permission_14 = Permission()
    auth_permission_14.name = u'Can delete permission'
    auth_permission_14.content_type = ContentType.objects.get(app_label="auth", model="permission")
    auth_permission_14.codename = u'delete_permission'
    auth_permission_14.save()

    auth_permission_15 = Permission()
    auth_permission_15.name = u'Can delete user'
    auth_permission_15.content_type = ContentType.objects.get(app_label="auth", model="user")
    auth_permission_15.codename = u'delete_user'
    auth_permission_15.save()

    auth_permission_16 = Permission()
    auth_permission_16.name = u'Can add almacen'
    auth_permission_16.content_type = ContentType.objects.get(app_label="central", model="almacen")
    auth_permission_16.codename = u'add_almacen'
    auth_permission_16.save()

    auth_permission_17 = Permission()
    auth_permission_17.name = u'Can add doc pedido'
    auth_permission_17.content_type = ContentType.objects.get(app_label="central", model="docpedido")
    auth_permission_17.codename = u'add_docpedido'
    auth_permission_17.save()

    auth_permission_18 = Permission()
    auth_permission_18.name = u'Can add linea doc pedido'
    auth_permission_18.content_type = ContentType.objects.get(app_label="central", model="lineadocpedido")
    auth_permission_18.codename = u'add_lineadocpedido'
    auth_permission_18.save()

    auth_permission_19 = Permission()
    auth_permission_19.name = u'Can add precio producto'
    auth_permission_19.content_type = ContentType.objects.get(app_label="central", model="precioproducto")
    auth_permission_19.codename = u'add_precioproducto'
    auth_permission_19.save()

    auth_permission_20 = Permission()
    auth_permission_20.name = u'Can add producto'
    auth_permission_20.content_type = ContentType.objects.get(app_label="central", model="producto")
    auth_permission_20.codename = u'add_producto'
    auth_permission_20.save()

    auth_permission_21 = Permission()
    auth_permission_21.name = u'Can change almacen'
    auth_permission_21.content_type = ContentType.objects.get(app_label="central", model="almacen")
    auth_permission_21.codename = u'change_almacen'
    auth_permission_21.save()

    auth_permission_22 = Permission()
    auth_permission_22.name = u'Can change doc pedido'
    auth_permission_22.content_type = ContentType.objects.get(app_label="central", model="docpedido")
    auth_permission_22.codename = u'change_docpedido'
    auth_permission_22.save()

    auth_permission_23 = Permission()
    auth_permission_23.name = u'Can change linea doc pedido'
    auth_permission_23.content_type = ContentType.objects.get(app_label="central", model="lineadocpedido")
    auth_permission_23.codename = u'change_lineadocpedido'
    auth_permission_23.save()

    auth_permission_24 = Permission()
    auth_permission_24.name = u'Can change precio producto'
    auth_permission_24.content_type = ContentType.objects.get(app_label="central", model="precioproducto")
    auth_permission_24.codename = u'change_precioproducto'
    auth_permission_24.save()

    auth_permission_25 = Permission()
    auth_permission_25.name = u'Can change producto'
    auth_permission_25.content_type = ContentType.objects.get(app_label="central", model="producto")
    auth_permission_25.codename = u'change_producto'
    auth_permission_25.save()

    auth_permission_26 = Permission()
    auth_permission_26.name = u'Can delete almacen'
    auth_permission_26.content_type = ContentType.objects.get(app_label="central", model="almacen")
    auth_permission_26.codename = u'delete_almacen'
    auth_permission_26.save()

    auth_permission_27 = Permission()
    auth_permission_27.name = u'Can delete doc pedido'
    auth_permission_27.content_type = ContentType.objects.get(app_label="central", model="docpedido")
    auth_permission_27.codename = u'delete_docpedido'
    auth_permission_27.save()

    auth_permission_28 = Permission()
    auth_permission_28.name = u'Can delete linea doc pedido'
    auth_permission_28.content_type = ContentType.objects.get(app_label="central", model="lineadocpedido")
    auth_permission_28.codename = u'delete_lineadocpedido'
    auth_permission_28.save()

    auth_permission_29 = Permission()
    auth_permission_29.name = u'Can delete precio producto'
    auth_permission_29.content_type = ContentType.objects.get(app_label="central", model="precioproducto")
    auth_permission_29.codename = u'delete_precioproducto'
    auth_permission_29.save()

    auth_permission_30 = Permission()
    auth_permission_30.name = u'Can delete producto'
    auth_permission_30.content_type = ContentType.objects.get(app_label="central", model="producto")
    auth_permission_30.codename = u'delete_producto'
    auth_permission_30.save()

    auth_permission_31 = Permission()
    auth_permission_31.name = u'Can add content type'
    auth_permission_31.content_type = ContentType.objects.get(app_label="contenttypes", model="contenttype")
    auth_permission_31.codename = u'add_contenttype'
    auth_permission_31.save()

    auth_permission_32 = Permission()
    auth_permission_32.name = u'Can change content type'
    auth_permission_32.content_type = ContentType.objects.get(app_label="contenttypes", model="contenttype")
    auth_permission_32.codename = u'change_contenttype'
    auth_permission_32.save()

    auth_permission_33 = Permission()
    auth_permission_33.name = u'Can delete content type'
    auth_permission_33.content_type = ContentType.objects.get(app_label="contenttypes", model="contenttype")
    auth_permission_33.codename = u'delete_contenttype'
    auth_permission_33.save()

    auth_permission_34 = Permission()
    auth_permission_34.name = u'Can add session'
    auth_permission_34.content_type = ContentType.objects.get(app_label="sessions", model="session")
    auth_permission_34.codename = u'add_session'
    auth_permission_34.save()

    auth_permission_35 = Permission()
    auth_permission_35.name = u'Can change session'
    auth_permission_35.content_type = ContentType.objects.get(app_label="sessions", model="session")
    auth_permission_35.codename = u'change_session'
    auth_permission_35.save()

    auth_permission_36 = Permission()
    auth_permission_36.name = u'Can delete session'
    auth_permission_36.content_type = ContentType.objects.get(app_label="sessions", model="session")
    auth_permission_36.codename = u'delete_session'
    auth_permission_36.save()

    auth_permission_37 = Permission()
    auth_permission_37.name = u'Can add site'
    auth_permission_37.content_type = ContentType.objects.get(app_label="sites", model="site")
    auth_permission_37.codename = u'add_site'
    auth_permission_37.save()

    auth_permission_38 = Permission()
    auth_permission_38.name = u'Can change site'
    auth_permission_38.content_type = ContentType.objects.get(app_label="sites", model="site")
    auth_permission_38.codename = u'change_site'
    auth_permission_38.save()

    auth_permission_39 = Permission()
    auth_permission_39.name = u'Can delete site'
    auth_permission_39.content_type = ContentType.objects.get(app_label="sites", model="site")
    auth_permission_39.codename = u'delete_site'
    auth_permission_39.save()

    from django.contrib.auth.models import Group

    auth_group_1 = Group()
    auth_group_1.name = u'Almacenes'
    auth_group_1.save()

    auth_group_1.permissions.add(auth_permission_17)
    auth_group_1.permissions.add(auth_permission_18)

    from django.contrib.auth.models import User

    auth_user_1 = User()
    auth_user_1.username = u'central'
    auth_user_1.first_name = u''
    auth_user_1.last_name = u''
    auth_user_1.email = u'central@centralcompras.com'
    auth_user_1.password = u'sha1$9e3fb$7d05aa7139d9cfb372efef78a7d90028ceb4b2e8'
    auth_user_1.is_staff = True
    auth_user_1.is_active = True
    auth_user_1.is_superuser = True
    auth_user_1.last_login = datetime.datetime(2009, 5, 25, 13, 54, 44, 851187)
    auth_user_1.date_joined = datetime.datetime(2009, 5, 25, 13, 26, 3, 911020)
    auth_user_1.save()

    from django.contrib.auth.models import Message


    from django.contrib.sessions.models import Session

    django_session_1 = Session()
    django_session_1.session_key = u'25152c11745a5161c2e1fc2f7f56df87'
    django_session_1.session_data = u'gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEESwF1LjBmZDJhZmJlYjMwMThhOWY2NzY4\nM2Q3M2NmNWUxYmNi\n'
    django_session_1.expire_date = datetime.datetime(2009, 6, 8, 13, 54, 44, 876349)
    django_session_1.save()

    from django.contrib.sites.models import Site

    django_site_1 = Site()
    django_site_1.domain = u'example.com'
    django_site_1.name = u'example.com'
    django_site_1.save()

    from django.contrib.admin.models import LogEntry

    django_admin_log_1 = LogEntry()
    django_admin_log_1.action_time = datetime.datetime(2009, 5, 26, 12, 14, 37, 413897)
    django_admin_log_1.user = auth_user_1
    django_admin_log_1.content_type = ContentType.objects.get(app_label="central", model="producto")
    django_admin_log_1.object_id = u'13'
    django_admin_log_1.object_repr = u'Ron'
    django_admin_log_1.action_flag = 3
    django_admin_log_1.change_message = u''
    django_admin_log_1.save()

    django_admin_log_2 = LogEntry()
    django_admin_log_2.action_time = datetime.datetime(2009, 5, 26, 12, 14, 37, 409425)
    django_admin_log_2.user = auth_user_1
    django_admin_log_2.content_type = ContentType.objects.get(app_label="central", model="producto")
    django_admin_log_2.object_id = u'14'
    django_admin_log_2.object_repr = u'Vodka'
    django_admin_log_2.action_flag = 3
    django_admin_log_2.change_message = u''
    django_admin_log_2.save()

    django_admin_log_3 = LogEntry()
    django_admin_log_3.action_time = datetime.datetime(2009, 5, 26, 12, 14, 37, 400973)
    django_admin_log_3.user = auth_user_1
    django_admin_log_3.content_type = ContentType.objects.get(app_label="central", model="producto")
    django_admin_log_3.object_id = u'15'
    django_admin_log_3.object_repr = u'Ginebra'
    django_admin_log_3.action_flag = 3
    django_admin_log_3.change_message = u''
    django_admin_log_3.save()

    django_admin_log_4 = LogEntry()
    django_admin_log_4.action_time = datetime.datetime(2009, 5, 26, 12, 14, 37, 389077)
    django_admin_log_4.user = auth_user_1
    django_admin_log_4.content_type = ContentType.objects.get(app_label="central", model="producto")
    django_admin_log_4.object_id = u'16'
    django_admin_log_4.object_repr = u'Shake'
    django_admin_log_4.action_flag = 3
    django_admin_log_4.change_message = u''
    django_admin_log_4.save()

    django_admin_log_5 = LogEntry()
    django_admin_log_5.action_time = datetime.datetime(2009, 5, 26, 12, 13, 5, 749075)
    django_admin_log_5.user = auth_user_1
    django_admin_log_5.content_type = ContentType.objects.get(app_label="central", model="precioproducto")
    django_admin_log_5.object_id = u'17'
    django_admin_log_5.object_repr = u'Whisky :: hasta 500 uds :: 6.00'
    django_admin_log_5.action_flag = 1
    django_admin_log_5.change_message = u''
    django_admin_log_5.save()

    django_admin_log_6 = LogEntry()
    django_admin_log_6.action_time = datetime.datetime(2009, 5, 26, 12, 12, 55, 947093)
    django_admin_log_6.user = auth_user_1
    django_admin_log_6.content_type = ContentType.objects.get(app_label="central", model="precioproducto")
    django_admin_log_6.object_id = u'16'
    django_admin_log_6.object_repr = u'Whisky :: hasta 300 uds :: 7.00'
    django_admin_log_6.action_flag = 1
    django_admin_log_6.change_message = u''
    django_admin_log_6.save()

    django_admin_log_7 = LogEntry()
    django_admin_log_7.action_time = datetime.datetime(2009, 5, 26, 12, 12, 40, 842643)
    django_admin_log_7.user = auth_user_1
    django_admin_log_7.content_type = ContentType.objects.get(app_label="central", model="precioproducto")
    django_admin_log_7.object_id = u'15'
    django_admin_log_7.object_repr = u'Whisky :: hasta 100 uds :: 8.00'
    django_admin_log_7.action_flag = 1
    django_admin_log_7.change_message = u''
    django_admin_log_7.save()

    django_admin_log_8 = LogEntry()
    django_admin_log_8.action_time = datetime.datetime(2009, 5, 26, 12, 12, 9, 831799)
    django_admin_log_8.user = auth_user_1
    django_admin_log_8.content_type = ContentType.objects.get(app_label="central", model="precioproducto")
    django_admin_log_8.object_id = u'14'
    django_admin_log_8.object_repr = u'Arroz :: hasta 3500 uds :: 0.50'
    django_admin_log_8.action_flag = 1
    django_admin_log_8.change_message = u''
    django_admin_log_8.save()

    django_admin_log_9 = LogEntry()
    django_admin_log_9.action_time = datetime.datetime(2009, 5, 26, 12, 11, 52, 67775)
    django_admin_log_9.user = auth_user_1
    django_admin_log_9.content_type = ContentType.objects.get(app_label="central", model="precioproducto")
    django_admin_log_9.object_id = u'13'
    django_admin_log_9.object_repr = u'Arroz :: hasta 1500 uds :: 0.75'
    django_admin_log_9.action_flag = 1
    django_admin_log_9.change_message = u''
    django_admin_log_9.save()

    django_admin_log_10 = LogEntry()
    django_admin_log_10.action_time = datetime.datetime(2009, 5, 26, 12, 11, 26, 536943)
    django_admin_log_10.user = auth_user_1
    django_admin_log_10.content_type = ContentType.objects.get(app_label="central", model="precioproducto")
    django_admin_log_10.object_id = u'12'
    django_admin_log_10.object_repr = u'Miel :: hasta 2000 uds :: 0.90'
    django_admin_log_10.action_flag = 1
    django_admin_log_10.change_message = u''
    django_admin_log_10.save()

    django_admin_log_11 = LogEntry()
    django_admin_log_11.action_time = datetime.datetime(2009, 5, 26, 12, 11, 14, 759357)
    django_admin_log_11.user = auth_user_1
    django_admin_log_11.content_type = ContentType.objects.get(app_label="central", model="precioproducto")
    django_admin_log_11.object_id = u'11'
    django_admin_log_11.object_repr = u'Miel :: hasta 1000 uds :: 1.00'
    django_admin_log_11.action_flag = 1
    django_admin_log_11.change_message = u''
    django_admin_log_11.save()

    django_admin_log_12 = LogEntry()
    django_admin_log_12.action_time = datetime.datetime(2009, 5, 26, 12, 10, 59, 4621)
    django_admin_log_12.user = auth_user_1
    django_admin_log_12.content_type = ContentType.objects.get(app_label="central", model="precioproducto")
    django_admin_log_12.object_id = u'10'
    django_admin_log_12.object_repr = u'Agua :: hasta 9999999999 uds :: 0.10'
    django_admin_log_12.action_flag = 1
    django_admin_log_12.change_message = u''
    django_admin_log_12.save()

    django_admin_log_13 = LogEntry()
    django_admin_log_13.action_time = datetime.datetime(2009, 5, 26, 12, 10, 32, 139367)
    django_admin_log_13.user = auth_user_1
    django_admin_log_13.content_type = ContentType.objects.get(app_label="central", model="precioproducto")
    django_admin_log_13.object_id = u'9'
    django_admin_log_13.object_repr = u'Agua :: hasta 5000 uds :: 0.15'
    django_admin_log_13.action_flag = 1
    django_admin_log_13.change_message = u''
    django_admin_log_13.save()

    django_admin_log_14 = LogEntry()
    django_admin_log_14.action_time = datetime.datetime(2009, 5, 26, 12, 10, 19, 749338)
    django_admin_log_14.user = auth_user_1
    django_admin_log_14.content_type = ContentType.objects.get(app_label="central", model="precioproducto")
    django_admin_log_14.object_id = u'8'
    django_admin_log_14.object_repr = u'Agua :: hasta 2000 uds :: 0.30'
    django_admin_log_14.action_flag = 1
    django_admin_log_14.change_message = u''
    django_admin_log_14.save()

    django_admin_log_15 = LogEntry()
    django_admin_log_15.action_time = datetime.datetime(2009, 5, 26, 12, 10, 8, 75818)
    django_admin_log_15.user = auth_user_1
    django_admin_log_15.content_type = ContentType.objects.get(app_label="central", model="precioproducto")
    django_admin_log_15.object_id = u'7'
    django_admin_log_15.object_repr = u'Pizza :: hasta 3000 uds :: 2.50'
    django_admin_log_15.action_flag = 1
    django_admin_log_15.change_message = u''
    django_admin_log_15.save()

    django_admin_log_16 = LogEntry()
    django_admin_log_16.action_time = datetime.datetime(2009, 5, 26, 12, 9, 55, 137395)
    django_admin_log_16.user = auth_user_1
    django_admin_log_16.content_type = ContentType.objects.get(app_label="central", model="precioproducto")
    django_admin_log_16.object_id = u'6'
    django_admin_log_16.object_repr = u'Pizza :: hasta 1500 uds :: 3.00'
    django_admin_log_16.action_flag = 1
    django_admin_log_16.change_message = u''
    django_admin_log_16.save()

    django_admin_log_17 = LogEntry()
    django_admin_log_17.action_time = datetime.datetime(2009, 5, 26, 12, 8, 52, 544597)
    django_admin_log_17.user = auth_user_1
    django_admin_log_17.content_type = ContentType.objects.get(app_label="central", model="producto")
    django_admin_log_17.object_id = u'17'
    django_admin_log_17.object_repr = u'Aguamiel'
    django_admin_log_17.action_flag = 1
    django_admin_log_17.change_message = u''
    django_admin_log_17.save()

    django_admin_log_18 = LogEntry()
    django_admin_log_18.action_time = datetime.datetime(2009, 5, 26, 12, 8, 44, 687262)
    django_admin_log_18.user = auth_user_1
    django_admin_log_18.content_type = ContentType.objects.get(app_label="central", model="producto")
    django_admin_log_18.object_id = u'16'
    django_admin_log_18.object_repr = u'Shake'
    django_admin_log_18.action_flag = 1
    django_admin_log_18.change_message = u''
    django_admin_log_18.save()

    django_admin_log_19 = LogEntry()
    django_admin_log_19.action_time = datetime.datetime(2009, 5, 26, 12, 8, 38, 941725)
    django_admin_log_19.user = auth_user_1
    django_admin_log_19.content_type = ContentType.objects.get(app_label="central", model="producto")
    django_admin_log_19.object_id = u'15'
    django_admin_log_19.object_repr = u'Ginebra'
    django_admin_log_19.action_flag = 1
    django_admin_log_19.change_message = u''
    django_admin_log_19.save()

    django_admin_log_20 = LogEntry()
    django_admin_log_20.action_time = datetime.datetime(2009, 5, 26, 12, 8, 34, 294218)
    django_admin_log_20.user = auth_user_1
    django_admin_log_20.content_type = ContentType.objects.get(app_label="central", model="producto")
    django_admin_log_20.object_id = u'14'
    django_admin_log_20.object_repr = u'Vodka'
    django_admin_log_20.action_flag = 1
    django_admin_log_20.change_message = u''
    django_admin_log_20.save()

    django_admin_log_21 = LogEntry()
    django_admin_log_21.action_time = datetime.datetime(2009, 5, 26, 12, 8, 24, 111170)
    django_admin_log_21.user = auth_user_1
    django_admin_log_21.content_type = ContentType.objects.get(app_label="central", model="producto")
    django_admin_log_21.object_id = u'13'
    django_admin_log_21.object_repr = u'Ron'
    django_admin_log_21.action_flag = 1
    django_admin_log_21.change_message = u''
    django_admin_log_21.save()

    django_admin_log_22 = LogEntry()
    django_admin_log_22.action_time = datetime.datetime(2009, 5, 26, 12, 8, 17, 159244)
    django_admin_log_22.user = auth_user_1
    django_admin_log_22.content_type = ContentType.objects.get(app_label="central", model="producto")
    django_admin_log_22.object_id = u'12'
    django_admin_log_22.object_repr = u'Whisky'
    django_admin_log_22.action_flag = 1
    django_admin_log_22.change_message = u''
    django_admin_log_22.save()

    django_admin_log_23 = LogEntry()
    django_admin_log_23.action_time = datetime.datetime(2009, 5, 26, 12, 7, 54, 701621)
    django_admin_log_23.user = auth_user_1
    django_admin_log_23.content_type = ContentType.objects.get(app_label="central", model="producto")
    django_admin_log_23.object_id = u'11'
    django_admin_log_23.object_repr = u'Ordenador'
    django_admin_log_23.action_flag = 1
    django_admin_log_23.change_message = u''
    django_admin_log_23.save()

    django_admin_log_24 = LogEntry()
    django_admin_log_24.action_time = datetime.datetime(2009, 5, 26, 12, 7, 44, 542111)
    django_admin_log_24.user = auth_user_1
    django_admin_log_24.content_type = ContentType.objects.get(app_label="central", model="producto")
    django_admin_log_24.object_id = u'10'
    django_admin_log_24.object_repr = u'Neveras'
    django_admin_log_24.action_flag = 1
    django_admin_log_24.change_message = u''
    django_admin_log_24.save()

    django_admin_log_25 = LogEntry()
    django_admin_log_25.action_time = datetime.datetime(2009, 5, 26, 12, 7, 30, 709611)
    django_admin_log_25.user = auth_user_1
    django_admin_log_25.content_type = ContentType.objects.get(app_label="central", model="producto")
    django_admin_log_25.object_id = u'9'
    django_admin_log_25.object_repr = u'Petardos (pumpum)'
    django_admin_log_25.action_flag = 1
    django_admin_log_25.change_message = u''
    django_admin_log_25.save()

    django_admin_log_26 = LogEntry()
    django_admin_log_26.action_time = datetime.datetime(2009, 5, 26, 12, 7, 19, 439150)
    django_admin_log_26.user = auth_user_1
    django_admin_log_26.content_type = ContentType.objects.get(app_label="central", model="producto")
    django_admin_log_26.object_id = u'8'
    django_admin_log_26.object_repr = u'Esteroides'
    django_admin_log_26.action_flag = 1
    django_admin_log_26.change_message = u''
    django_admin_log_26.save()

    django_admin_log_27 = LogEntry()
    django_admin_log_27.action_time = datetime.datetime(2009, 5, 26, 12, 7, 13, 289139)
    django_admin_log_27.user = auth_user_1
    django_admin_log_27.content_type = ContentType.objects.get(app_label="central", model="producto")
    django_admin_log_27.object_id = u'7'
    django_admin_log_27.object_repr = u'Barritas'
    django_admin_log_27.action_flag = 1
    django_admin_log_27.change_message = u''
    django_admin_log_27.save()

    django_admin_log_28 = LogEntry()
    django_admin_log_28.action_time = datetime.datetime(2009, 5, 26, 12, 7, 7, 981423)
    django_admin_log_28.user = auth_user_1
    django_admin_log_28.content_type = ContentType.objects.get(app_label="central", model="producto")
    django_admin_log_28.object_id = u'6'
    django_admin_log_28.object_repr = u'Arroz'
    django_admin_log_28.action_flag = 1
    django_admin_log_28.change_message = u''
    django_admin_log_28.save()

    django_admin_log_29 = LogEntry()
    django_admin_log_29.action_time = datetime.datetime(2009, 5, 26, 12, 7, 4, 321233)
    django_admin_log_29.user = auth_user_1
    django_admin_log_29.content_type = ContentType.objects.get(app_label="central", model="producto")
    django_admin_log_29.object_id = u'5'
    django_admin_log_29.object_repr = u'Miel'
    django_admin_log_29.action_flag = 1
    django_admin_log_29.change_message = u''
    django_admin_log_29.save()

    django_admin_log_30 = LogEntry()
    django_admin_log_30.action_time = datetime.datetime(2009, 5, 26, 12, 6, 58, 906543)
    django_admin_log_30.user = auth_user_1
    django_admin_log_30.content_type = ContentType.objects.get(app_label="central", model="producto")
    django_admin_log_30.object_id = u'4'
    django_admin_log_30.object_repr = u'Agua'
    django_admin_log_30.action_flag = 1
    django_admin_log_30.change_message = u''
    django_admin_log_30.save()

    django_admin_log_31 = LogEntry()
    django_admin_log_31.action_time = datetime.datetime(2009, 5, 26, 12, 6, 27, 983617)
    django_admin_log_31.user = auth_user_1
    django_admin_log_31.content_type = ContentType.objects.get(app_label="central", model="almacen")
    django_admin_log_31.object_id = u'6'
    django_admin_log_31.object_repr = u'Sepu'
    django_admin_log_31.action_flag = 1
    django_admin_log_31.change_message = u''
    django_admin_log_31.save()

    django_admin_log_32 = LogEntry()
    django_admin_log_32.action_time = datetime.datetime(2009, 5, 26, 12, 5, 13, 996437)
    django_admin_log_32.user = auth_user_1
    django_admin_log_32.content_type = ContentType.objects.get(app_label="central", model="almacen")
    django_admin_log_32.object_id = u'5'
    django_admin_log_32.object_repr = u'Simply'
    django_admin_log_32.action_flag = 1
    django_admin_log_32.change_message = u''
    django_admin_log_32.save()

    django_admin_log_33 = LogEntry()
    django_admin_log_33.action_time = datetime.datetime(2009, 5, 26, 12, 4, 20, 251890)
    django_admin_log_33.user = auth_user_1
    django_admin_log_33.content_type = ContentType.objects.get(app_label="central", model="almacen")
    django_admin_log_33.object_id = u'4'
    django_admin_log_33.object_repr = u'DIA'
    django_admin_log_33.action_flag = 1
    django_admin_log_33.change_message = u''
    django_admin_log_33.save()

    django_admin_log_34 = LogEntry()
    django_admin_log_34.action_time = datetime.datetime(2009, 5, 26, 11, 54, 45, 489325)
    django_admin_log_34.user = auth_user_1
    django_admin_log_34.content_type = ContentType.objects.get(app_label="central", model="docpedido")
    django_admin_log_34.object_id = u'2'
    django_admin_log_34.object_repr = u'2 :: Galerias Primero :: 2009-05-26 11:54:13.475758'
    django_admin_log_34.action_flag = 2
    django_admin_log_34.change_message = u'No ha cambiado ning\xfan campo.'
    django_admin_log_34.save()

    django_admin_log_35 = LogEntry()
    django_admin_log_35.action_time = datetime.datetime(2009, 5, 26, 11, 54, 13, 479907)
    django_admin_log_35.user = auth_user_1
    django_admin_log_35.content_type = ContentType.objects.get(app_label="central", model="docpedido")
    django_admin_log_35.object_id = u'2'
    django_admin_log_35.object_repr = u'2 :: Galerias Primero :: 2009-05-26 11:54:13.475758'
    django_admin_log_35.action_flag = 1
    django_admin_log_35.change_message = u''
    django_admin_log_35.save()

    django_admin_log_36 = LogEntry()
    django_admin_log_36.action_time = datetime.datetime(2009, 5, 26, 11, 53, 44, 886581)
    django_admin_log_36.user = auth_user_1
    django_admin_log_36.content_type = ContentType.objects.get(app_label="central", model="docpedido")
    django_admin_log_36.object_id = u'1'
    django_admin_log_36.object_repr = u'1 :: El Corte Ingles :: 2009-05-26 11:53:44.882515'
    django_admin_log_36.action_flag = 1
    django_admin_log_36.change_message = u''
    django_admin_log_36.save()

    django_admin_log_37 = LogEntry()
    django_admin_log_37.action_time = datetime.datetime(2009, 5, 26, 11, 48, 13, 366796)
    django_admin_log_37.user = auth_user_1
    django_admin_log_37.content_type = ContentType.objects.get(app_label="central", model="precioproducto")
    django_admin_log_37.object_id = u'5'
    django_admin_log_37.object_repr = u'Leche :: hasta 3000 uds :: 0.30'
    django_admin_log_37.action_flag = 1
    django_admin_log_37.change_message = u''
    django_admin_log_37.save()

    django_admin_log_38 = LogEntry()
    django_admin_log_38.action_time = datetime.datetime(2009, 5, 26, 11, 47, 52, 289089)
    django_admin_log_38.user = auth_user_1
    django_admin_log_38.content_type = ContentType.objects.get(app_label="central", model="precioproducto")
    django_admin_log_38.object_id = u'4'
    django_admin_log_38.object_repr = u'Leche :: hasta 2000 uds :: 0.40'
    django_admin_log_38.action_flag = 1
    django_admin_log_38.change_message = u''
    django_admin_log_38.save()

    django_admin_log_39 = LogEntry()
    django_admin_log_39.action_time = datetime.datetime(2009, 5, 26, 11, 47, 37, 147875)
    django_admin_log_39.user = auth_user_1
    django_admin_log_39.content_type = ContentType.objects.get(app_label="central", model="precioproducto")
    django_admin_log_39.object_id = u'3'
    django_admin_log_39.object_repr = u'Leche :: hasta 1000 uds :: 0.50'
    django_admin_log_39.action_flag = 1
    django_admin_log_39.change_message = u''
    django_admin_log_39.save()

    django_admin_log_40 = LogEntry()
    django_admin_log_40.action_time = datetime.datetime(2009, 5, 26, 11, 9, 13, 857133)
    django_admin_log_40.user = auth_user_1
    django_admin_log_40.content_type = ContentType.objects.get(app_label="central", model="precioproducto")
    django_admin_log_40.object_id = u'2'
    django_admin_log_40.object_repr = u'Yogures :: 0.90'
    django_admin_log_40.action_flag = 1
    django_admin_log_40.change_message = u''
    django_admin_log_40.save()

    django_admin_log_41 = LogEntry()
    django_admin_log_41.action_time = datetime.datetime(2009, 5, 26, 11, 8, 52, 794911)
    django_admin_log_41.user = auth_user_1
    django_admin_log_41.content_type = ContentType.objects.get(app_label="central", model="precioproducto")
    django_admin_log_41.object_id = u'1'
    django_admin_log_41.object_repr = u'Yogures :: 1.00'
    django_admin_log_41.action_flag = 1
    django_admin_log_41.change_message = u''
    django_admin_log_41.save()

    django_admin_log_42 = LogEntry()
    django_admin_log_42.action_time = datetime.datetime(2009, 5, 26, 11, 1, 26, 333375)
    django_admin_log_42.user = auth_user_1
    django_admin_log_42.content_type = ContentType.objects.get(app_label="central", model="producto")
    django_admin_log_42.object_id = u'3'
    django_admin_log_42.object_repr = u'Pizza'
    django_admin_log_42.action_flag = 1
    django_admin_log_42.change_message = u''
    django_admin_log_42.save()

    django_admin_log_43 = LogEntry()
    django_admin_log_43.action_time = datetime.datetime(2009, 5, 26, 11, 1, 7, 26477)
    django_admin_log_43.user = auth_user_1
    django_admin_log_43.content_type = ContentType.objects.get(app_label="central", model="producto")
    django_admin_log_43.object_id = u'2'
    django_admin_log_43.object_repr = u'Leche'
    django_admin_log_43.action_flag = 1
    django_admin_log_43.change_message = u''
    django_admin_log_43.save()

    django_admin_log_44 = LogEntry()
    django_admin_log_44.action_time = datetime.datetime(2009, 5, 26, 11, 1, 2, 570472)
    django_admin_log_44.user = auth_user_1
    django_admin_log_44.content_type = ContentType.objects.get(app_label="central", model="producto")
    django_admin_log_44.object_id = u'1'
    django_admin_log_44.object_repr = u'Yogures'
    django_admin_log_44.action_flag = 1
    django_admin_log_44.change_message = u''
    django_admin_log_44.save()

    django_admin_log_45 = LogEntry()
    django_admin_log_45.action_time = datetime.datetime(2009, 5, 25, 14, 19, 9, 731467)
    django_admin_log_45.user = auth_user_1
    django_admin_log_45.content_type = ContentType.objects.get(app_label="central", model="almacen")
    django_admin_log_45.object_id = u'3'
    django_admin_log_45.object_repr = u'Galerias Primero'
    django_admin_log_45.action_flag = 1
    django_admin_log_45.change_message = u''
    django_admin_log_45.save()

    django_admin_log_46 = LogEntry()
    django_admin_log_46.action_time = datetime.datetime(2009, 5, 25, 14, 17, 42, 218324)
    django_admin_log_46.user = auth_user_1
    django_admin_log_46.content_type = ContentType.objects.get(app_label="central", model="almacen")
    django_admin_log_46.object_id = u'2'
    django_admin_log_46.object_repr = u'El Corte Ingles'
    django_admin_log_46.action_flag = 1
    django_admin_log_46.change_message = u''
    django_admin_log_46.save()

    django_admin_log_47 = LogEntry()
    django_admin_log_47.action_time = datetime.datetime(2009, 5, 25, 14, 15, 2, 71108)
    django_admin_log_47.user = auth_user_1
    django_admin_log_47.content_type = ContentType.objects.get(app_label="auth", model="group")
    django_admin_log_47.object_id = u'1'
    django_admin_log_47.object_repr = u'Almacenes'
    django_admin_log_47.action_flag = 1
    django_admin_log_47.change_message = u''
    django_admin_log_47.save()

    django_admin_log_48 = LogEntry()
    django_admin_log_48.action_time = datetime.datetime(2009, 5, 25, 13, 57, 39, 742414)
    django_admin_log_48.user = auth_user_1
    django_admin_log_48.content_type = ContentType.objects.get(app_label="central", model="producto")
    django_admin_log_48.object_id = u'1'
    django_admin_log_48.object_repr = u'Yogures'
    django_admin_log_48.action_flag = 1
    django_admin_log_48.change_message = u''
    django_admin_log_48.save()

    from analisiscentralcompras.central.models import Almacen

    central_almacen_1 = Almacen()
    central_almacen_1.username = u'ci'
    central_almacen_1.first_name = u'Hijos de Onan'
    central_almacen_1.last_name = u'Kabrones'
    central_almacen_1.email = u'nomail@hahaha.com'
    central_almacen_1.password = u'abcABC1'
    central_almacen_1.is_staff = False
    central_almacen_1.is_active = True
    central_almacen_1.is_superuser = False
    central_almacen_1.last_login = datetime.datetime(2009, 5, 25, 14, 6, 35)
    central_almacen_1.date_joined = datetime.datetime(2009, 5, 25, 14, 6, 35)
    central_almacen_1.nombre = u'El Corte Ingles'
    central_almacen_1.estado = u'A'
    central_almacen_1.direccion = u'xxxxxxxxxxxxxxxxxx'
    central_almacen_1.fecha_alta = datetime.date(2009, 5, 25)
    central_almacen_1.fecha_baja = None
    central_almacen_1.save()

    central_almacen_1.groups.add(auth_group_1)

    central_almacen_2 = Almacen()
    central_almacen_2.username = u'galerias'
    central_almacen_2.first_name = u''
    central_almacen_2.last_name = u''
    central_almacen_2.email = u''
    central_almacen_2.password = u'abcABC1'
    central_almacen_2.is_staff = False
    central_almacen_2.is_active = True
    central_almacen_2.is_superuser = False
    central_almacen_2.last_login = datetime.datetime(2009, 5, 25, 14, 18, 25)
    central_almacen_2.date_joined = datetime.datetime(2009, 5, 25, 14, 18, 25)
    central_almacen_2.nombre = u'Galerias Primero'
    central_almacen_2.estado = u'A'
    central_almacen_2.direccion = u'Zaragoza'
    central_almacen_2.fecha_alta = datetime.date(2009, 5, 25)
    central_almacen_2.fecha_baja = None
    central_almacen_2.save()

    central_almacen_2.groups.add(auth_group_1)

    central_almacen_3 = Almacen()
    central_almacen_3.username = u'dia'
    central_almacen_3.first_name = u'DIA'
    central_almacen_3.last_name = u''
    central_almacen_3.email = u''
    central_almacen_3.password = u'abcABC1'
    central_almacen_3.is_staff = False
    central_almacen_3.is_active = True
    central_almacen_3.is_superuser = False
    central_almacen_3.last_login = datetime.datetime(2009, 5, 26, 12, 3, 34)
    central_almacen_3.date_joined = datetime.datetime(2009, 5, 26, 12, 3, 34)
    central_almacen_3.nombre = u'DIA'
    central_almacen_3.estado = u'A'
    central_almacen_3.direccion = u'nose'
    central_almacen_3.fecha_alta = datetime.date(2009, 5, 26)
    central_almacen_3.fecha_baja = None
    central_almacen_3.save()

    central_almacen_4 = Almacen()
    central_almacen_4.username = u'simply'
    central_almacen_4.first_name = u''
    central_almacen_4.last_name = u''
    central_almacen_4.email = u''
    central_almacen_4.password = u'abcABC1'
    central_almacen_4.is_staff = False
    central_almacen_4.is_active = True
    central_almacen_4.is_superuser = False
    central_almacen_4.last_login = datetime.datetime(2009, 5, 26, 12, 4, 20)
    central_almacen_4.date_joined = datetime.datetime(2009, 5, 26, 12, 4, 20)
    central_almacen_4.nombre = u'Simply'
    central_almacen_4.estado = u'A'
    central_almacen_4.direccion = u'Cuenca'
    central_almacen_4.fecha_alta = datetime.date(2009, 5, 26)
    central_almacen_4.fecha_baja = None
    central_almacen_4.save()

    central_almacen_5 = Almacen()
    central_almacen_5.username = u'sepu'
    central_almacen_5.first_name = u''
    central_almacen_5.last_name = u''
    central_almacen_5.email = u''
    central_almacen_5.password = u'abcABC1'
    central_almacen_5.is_staff = False
    central_almacen_5.is_active = True
    central_almacen_5.is_superuser = False
    central_almacen_5.last_login = datetime.datetime(2009, 5, 26, 12, 5, 14)
    central_almacen_5.date_joined = datetime.datetime(2009, 5, 26, 12, 5, 14)
    central_almacen_5.nombre = u'Sepu'
    central_almacen_5.estado = u'B'
    central_almacen_5.direccion = u'murcia'
    central_almacen_5.fecha_alta = datetime.date(1945, 2, 11)
    central_almacen_5.fecha_baja = datetime.date(1999, 10, 19)
    central_almacen_5.save()

    from analisiscentralcompras.central.models import DocPedido

    central_docpedido_1 = DocPedido()
    central_docpedido_1.fecha = datetime.datetime(2009, 5, 26, 11, 53, 44, 882515)
    central_docpedido_1.almacen = central_almacen_1
    central_docpedido_1.save()

    central_docpedido_2 = DocPedido()
    central_docpedido_2.fecha = datetime.datetime(2009, 5, 26, 11, 54, 13, 475758)
    central_docpedido_2.almacen = central_almacen_2
    central_docpedido_2.save()

    from analisiscentralcompras.central.models import Producto

    central_producto_1 = Producto()
    central_producto_1.nombre = u'Yogures'
    central_producto_1.save()

    central_producto_2 = Producto()
    central_producto_2.nombre = u'Leche'
    central_producto_2.save()

    central_producto_3 = Producto()
    central_producto_3.nombre = u'Pizza'
    central_producto_3.save()

    central_producto_4 = Producto()
    central_producto_4.nombre = u'Agua'
    central_producto_4.save()

    central_producto_5 = Producto()
    central_producto_5.nombre = u'Miel'
    central_producto_5.save()

    central_producto_6 = Producto()
    central_producto_6.nombre = u'Arroz'
    central_producto_6.save()

    central_producto_7 = Producto()
    central_producto_7.nombre = u'Barritas'
    central_producto_7.save()

    central_producto_8 = Producto()
    central_producto_8.nombre = u'Esteroides'
    central_producto_8.save()

    central_producto_9 = Producto()
    central_producto_9.nombre = u'Petardos (pumpum)'
    central_producto_9.save()

    central_producto_10 = Producto()
    central_producto_10.nombre = u'Neveras'
    central_producto_10.save()

    central_producto_11 = Producto()
    central_producto_11.nombre = u'Ordenador'
    central_producto_11.save()

    central_producto_12 = Producto()
    central_producto_12.nombre = u'Whisky'
    central_producto_12.save()

    central_producto_13 = Producto()
    central_producto_13.nombre = u'Aguamiel'
    central_producto_13.save()

    central_producto_14 = Producto()
    central_producto_14.nombre = u'Ron'
    central_producto_14.save()

    central_producto_15 = Producto()
    central_producto_15.nombre = u'Vodka'
    central_producto_15.save()

    central_producto_16 = Producto()
    central_producto_16.nombre = u'Ginebra'
    central_producto_16.save()

    central_producto_17 = Producto()
    central_producto_17.nombre = u'Red Bull'
    central_producto_17.save()

    central_producto_18 = Producto()
    central_producto_18.nombre = u'Pacharan'
    central_producto_18.save()

    from analisiscentralcompras.central.models import PrecioProducto

    central_precioproducto_1 = PrecioProducto()
    central_precioproducto_1.producto = central_producto_1
    central_precioproducto_1.precio = Decimal('1')
    central_precioproducto_1.cantidad = 1000
    central_precioproducto_1.save()

    central_precioproducto_2 = PrecioProducto()
    central_precioproducto_2.producto = central_producto_1
    central_precioproducto_2.precio = Decimal('0.9')
    central_precioproducto_2.cantidad = 2000
    central_precioproducto_2.save()

    central_precioproducto_3 = PrecioProducto()
    central_precioproducto_3.producto = central_producto_2
    central_precioproducto_3.precio = Decimal('0.5')
    central_precioproducto_3.cantidad = 1000
    central_precioproducto_3.save()

    central_precioproducto_4 = PrecioProducto()
    central_precioproducto_4.producto = central_producto_2
    central_precioproducto_4.precio = Decimal('0.4')
    central_precioproducto_4.cantidad = 2000
    central_precioproducto_4.save()

    central_precioproducto_5 = PrecioProducto()
    central_precioproducto_5.producto = central_producto_2
    central_precioproducto_5.precio = Decimal('0.3')
    central_precioproducto_5.cantidad = 3000
    central_precioproducto_5.save()

    central_precioproducto_6 = PrecioProducto()
    central_precioproducto_6.producto = central_producto_3
    central_precioproducto_6.precio = Decimal('3')
    central_precioproducto_6.cantidad = 1500
    central_precioproducto_6.save()

    central_precioproducto_7 = PrecioProducto()
    central_precioproducto_7.producto = central_producto_3
    central_precioproducto_7.precio = Decimal('2.5')
    central_precioproducto_7.cantidad = 3000
    central_precioproducto_7.save()

    central_precioproducto_8 = PrecioProducto()
    central_precioproducto_8.producto = central_producto_4
    central_precioproducto_8.precio = Decimal('0.3')
    central_precioproducto_8.cantidad = 2000
    central_precioproducto_8.save()

    central_precioproducto_9 = PrecioProducto()
    central_precioproducto_9.producto = central_producto_4
    central_precioproducto_9.precio = Decimal('0.15')
    central_precioproducto_9.cantidad = 5000
    central_precioproducto_9.save()

    central_precioproducto_10 = PrecioProducto()
    central_precioproducto_10.producto = central_producto_4
    central_precioproducto_10.precio = Decimal('0.1')
    central_precioproducto_10.cantidad = 9999999999L
    central_precioproducto_10.save()

    central_precioproducto_11 = PrecioProducto()
    central_precioproducto_11.producto = central_producto_5
    central_precioproducto_11.precio = Decimal('1')
    central_precioproducto_11.cantidad = 1000
    central_precioproducto_11.save()

    central_precioproducto_12 = PrecioProducto()
    central_precioproducto_12.producto = central_producto_5
    central_precioproducto_12.precio = Decimal('0.9')
    central_precioproducto_12.cantidad = 2000
    central_precioproducto_12.save()

    central_precioproducto_13 = PrecioProducto()
    central_precioproducto_13.producto = central_producto_6
    central_precioproducto_13.precio = Decimal('0.75')
    central_precioproducto_13.cantidad = 1500
    central_precioproducto_13.save()

    central_precioproducto_14 = PrecioProducto()
    central_precioproducto_14.producto = central_producto_6
    central_precioproducto_14.precio = Decimal('0.5')
    central_precioproducto_14.cantidad = 3500
    central_precioproducto_14.save()

    central_precioproducto_15 = PrecioProducto()
    central_precioproducto_15.producto = central_producto_12
    central_precioproducto_15.precio = Decimal('8')
    central_precioproducto_15.cantidad = 100
    central_precioproducto_15.save()

    central_precioproducto_16 = PrecioProducto()
    central_precioproducto_16.producto = central_producto_12
    central_precioproducto_16.precio = Decimal('7')
    central_precioproducto_16.cantidad = 300
    central_precioproducto_16.save()

    central_precioproducto_17 = PrecioProducto()
    central_precioproducto_17.producto = central_producto_12
    central_precioproducto_17.precio = Decimal('6')
    central_precioproducto_17.cantidad = 500
    central_precioproducto_17.save()

    from analisiscentralcompras.central.models import LineaDocPedido

    central_lineadocpedido_1 = LineaDocPedido()
    central_lineadocpedido_1.docpedido = central_docpedido_1
    central_lineadocpedido_1.producto = central_producto_1
    central_lineadocpedido_1.cantidad = 1500
    central_lineadocpedido_1.save()

    central_lineadocpedido_2 = LineaDocPedido()
    central_lineadocpedido_2.docpedido = central_docpedido_1
    central_lineadocpedido_2.producto = central_producto_2
    central_lineadocpedido_2.cantidad = 3000
    central_lineadocpedido_2.save()

    central_lineadocpedido_3 = LineaDocPedido()
    central_lineadocpedido_3.docpedido = central_docpedido_2
    central_lineadocpedido_3.producto = central_producto_2
    central_lineadocpedido_3.cantidad = 500
    central_lineadocpedido_3.save()

    central_lineadocpedido_4 = LineaDocPedido()
    central_lineadocpedido_4.docpedido = central_docpedido_2
    central_lineadocpedido_4.producto = central_producto_1
    central_lineadocpedido_4.cantidad = 900
    central_lineadocpedido_4.save()

