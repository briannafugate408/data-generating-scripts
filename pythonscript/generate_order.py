import random
import names
import string
import json
import randomtimestamp
from datetime import datetime

def create_random_order_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=25))

def create_random_recipe_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=25))

def create_orderitem_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=25))

def get_random_order_type():
    order_types = ["BATCH", "DIRECT_INTEGRATION_QSR"]
    return random.choice(order_types)

def get_random_total_order_items():
    return random.randint(1, 5)

def get_random_index(total_order_items):
    return random.randint(1, total_order_items)

def get_random_item_name():
    item_names = ["Chicken Bowl", "Caesar Salad", "Fruit Salad", "Bean Bowl", "Thai Bowl"]
    return random.choice(item_names)

def get_random_external_entree_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=15))

def get_random_order_customer_name():
    order_customer_name = ["DoorDash", "Samsara", "Tesla", "Ford", "Amazon", "Google", "Vanguard", "Apple", "Microsoft", "IBM", "UNLV", "Integration Team", "Hardware Team", "Intuit-operations", "Legal-ops", "Finance-ops", "HR-ops", "Marketing-ops", "Sales-ops", "Product-ops", "Engineering-ops", "Customer-ops", "Support-ops", "Security-ops", "Compliance-ops", "Data-ops", "IT-ops", "Procurement-ops", "Facilities-ops", "Real-estate-ops", "Admin-ops", "Executive-ops", "Business-ops", "Strategy-ops", "Partnership-ops", "Alliance-ops", "Channel-ops", "Distribution-ops", "Logistics-ops", "Supply-chain-ops", "Manufacturing-ops", "Production-ops", "Quality-ops", "Testing-ops", "R&D-ops", "Innovation-ops", "Product-management-ops", "Project-management-ops", "Program-management-ops", "Portfolio-management-ops", "PMO-ops", "Agile-ops", "Scrum-ops", "Kanban-ops", "Lean-ops", "Six-sigma-ops", "DevOps-ops", "SRE-ops", "Site-reliability-ops", "Cloud-ops", "AWS-ops", "Azure-ops", "GCP-ops", "IBM-cloud-ops", "Oracle-cloud-ops", "Alibaba-cloud-ops", "Tencent-cloud-ops", "Baidu-cloud-ops", "Salesforce-ops", "ServiceNow-ops", "Workday-ops", "Slack-ops", "Zoom-ops", "Webex-ops", "Teams-ops", "Jira-ops", "Confluence-ops", "Bitbucket-ops", "Github-ops", "Gitlab-ops", "Docker-ops", "Kubernetes-ops", "Terraform-ops", "Ansible-ops", "Chef-ops", "Puppet-ops", "Splunk-ops", "Datadog-ops", "NewRelic-ops", "AppDynamics-ops", "Dynatrace-ops", "SumoLogic-ops", "Loggly-ops", "Logz.io-ops", "Elastic-ops", "Kibana-ops", "Logstash-ops", "Beats-ops", "Prometheus-ops", "Grafana-ops",]
    return random.choice(order_customer_name)

def make_order_obj():
    total_order_items = get_random_total_order_items()
    created_at_time = int(datetime.timestamp(randomtimestamp.randomtimestamp(start_year=2023, text=False)))
    promise_time = int(created_at_time + 900)

    customer_name = names.get_full_name()

    order_item = {
        "itemCustomerName": customer_name,
        "orderType": get_random_order_type(),
        "totalItems": total_order_items,
        "orderId": str(create_random_order_id()),
        "index": get_random_index(total_order_items),
        "itemNote": "", 
        "recipeId": str(create_random_recipe_id()),
        "totalProductionItems": total_order_items,
        "itemName": get_random_item_name(),
        "promiseTimeMs": promise_time,
        "createdTimeMs": created_at_time,
        "id": create_orderitem_id(),
        "externalEntreeId": get_random_external_entree_id(),
        "orderCustomerName": customer_name,
        "ddb_stream_event_type": "insert",
        "dimension_event_type": "insert",
        "created_at_ms": created_at_time,
    }
    return order_item

def write_order_obj(order, i):
    with open("order-" + str(i) + ".json", "w") as f:
          json.dump(order, f)


print("Generating orders")
order = make_order_obj()
print(order)

for i in range(5000, 20000):
    order = make_order_obj()
    print(order)
    write_order_obj(order, i)