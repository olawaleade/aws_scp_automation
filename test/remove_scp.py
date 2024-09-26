import boto3

# Initialize a session using Amazon Organizations
client = boto3.client('organizations')

# Initialize a session using the admin profile
#session = boto3.Session(profile_name='admin')
#client = session.client('organizations')

# The ID of the root OU
root_ou_id = 'root-ou-id'
compliant_ou_id = 'compliant-ou-id'

# Policies to be attached to the root OU
root_policies = ['gp87', 'gp80', 'gp64']

# Policies to be attached to the compliant OU
compliant_policies = ['gp61', 'gp63', 'gp71', 'gp74']

# Function to detach and delete policies
def detach_and_delete_policy(policy_id, target_ou_id):

    # Detach the SCP policy from the target OU
    client.detach_policy(
        PolicyId=policy_id,
        TargetId=target_ou_id
    )
    print(f"Policy {policy_id} has been detached from OU {target_ou_id}.")
    
    # Delete the SCP policy
    client.delete_policy(
        PolicyId=policy_id
    )
    print(f"Policy {policy_id} has been deleted.")

# Function to list and detach policies for a given OU
def list_and_detach_policies(target_ou_id, policy_names):
    paginator = client.get_paginator('list_policies_for_target')
    for page in paginator.paginate(TargetId=target_ou_id, Filter='SERVICE_CONTROL_POLICY'):
        for policy in page['Policies']:
            policy_name = policy['Name']
            policy_id = policy['Id']
            if policy_name in policy_names:
                detach_and_delete_policy(policy_id, target_ou_id)

# Detach and delete policies from the root OU
list_and_detach_policies(root_ou_id, root_policies)

# Detach and delete policies from the child OU
list_and_detach_policies(compliant_ou_id, compliant_policies)

print("All specified policies have been detached and deleted.")
