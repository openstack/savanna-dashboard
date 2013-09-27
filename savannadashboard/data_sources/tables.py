# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright (c) 2013 Red Hat Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging

from django.utils.translation import ugettext_lazy as _

from horizon import tables

from savannadashboard.api.client import client as savannaclient

LOG = logging.getLogger(__name__)


class CreateDataSource(tables.LinkAction):
    name = "create data source"
    verbose_name = _("Create Data Source")
    url = "horizon:savanna:data_sources:create-data-source"
    classes = ("btn-launch", "ajax-modal")


class DeleteDataSource(tables.BatchAction):
    name = "delete"
    action_present = _("Delete")
    action_past = _("Deleted")
    data_type_singular = _("Data source")
    data_type_plural = _("Data sources")
    classes = ('btn-danger', 'btn-terminate')

    def action(self, request, obj_id):
        savanna = savannaclient(request)
        savanna.data_sources.delete(obj_id)


class DataSourcesTable(tables.DataTable):
    name = tables.Column("name",
                         verbose_name=_("Name"),
                         link=("horizon:savanna:data_sources:details"))
    type = tables.Column("type",
                         verbose_name=_("Type"))
    description = tables.Column("description",
                                verbose_name=_("Description"))

    class Meta:
        name = "data_sources"
        verbose_name = _("Data Sources")
        table_actions = (CreateDataSource,
                         DeleteDataSource)
        row_actions = (DeleteDataSource,)
