#!/bin/bash

# This script will be executed inside pre_test_hook function in devstack gate

set -ex
source commons $@

cd /opt/stack/new/horizon/openstack_dashboard/local/local_settings.d
mv _20_integration_tests_scaffolds.py.example _20_integration_tests_scaffolds.py

mv _2010_integration_tests_deprecated.py.example _2010_integration_tests_deprecated.py
cat > /opt/stack/new/horizon/openstack_dashboard/test/integration_tests/local-horizon.conf <<EOF
[image]
panel_type=legacy

[flavors]
panel_type=legacy
EOF

