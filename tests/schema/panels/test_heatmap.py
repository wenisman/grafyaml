# Copyright 2015 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from testtools import TestCase

from grafana_dashboards.schema.panel.heatmap import Heatmap


class TestCaseHeatmap(TestCase):
    def setUp(self):
        super(TestCaseHeatmap, self).setUp()
        self.schema = Heatmap().get_schema()

    def test_defaults(self):
        # Ensure default values get parsed correctly.
        defaults = {
            "color": {
                "cardColor": "#b4ff00",
                "colorScale": "sqrt",
                "colorScheme": "interpolatedOranges",
                "exponent": 0.5,
                "mode": "opacity",
            },
            "editable": True,
            "error": False,
            "span": 12,
            "tooltip": {
                "show": True,
                "showHistogram": True,
            },
            "xAxis": {"show": True},
            "yAxis": {
                "format": "short",
                "logBase": 1,
                "show": True,
            },
            "targets": [],
            "title": "foobar",
            "type": "heatmap",
        }
        self.assertEqual(self.schema(defaults), defaults)
