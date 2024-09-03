#!/bin/bash

# Function to test connectivity
test_connectivity() {
    from=$1
    to=$2
    echo "Testing connectivity from $from to $to"
    kubectl exec -n circular-traffic test-pod -- wget -qO- --timeout=2 http://$to
    if [ $? -eq 0 ]; then
        echo "Connection successful"
    else
        echo "Connection failed"
    fi
    echo
}

# Test all possible connections
for from in service-a service-b service-c; do
    for to in service-a service-b service-c; do
        test_connectivity $from $to
    done
done