import boto3
import json
import os

# Initialize a session using Amazon Organizations
client = boto3.client('organizations')

# Initialize a session using the admin profile
#session = boto3.Session(profile_name='admin')
#client = session.client('organizations')

# Define the path to the policies folder
policies_folder_path = os.path.join(os.path.dirname(__file__), '../policies/aws')


# Define the OU IDs
root_ou_id = 'ou-8p2j-dm62c9gv'
compliant_ou_id = 'ou-8p2j-h9va4zd1'

# Policies to be attached to the root OU
root_policies = ['gp87.json', 'gp80.json', 'gp64.json']

# Policies to be attached to the compliant OU
compliant_policies = ['gp61.json', 'gp63.json', 'gp71.json', 'gp74.json']

# Function to create and attach policies
def create_and_attach_policy(policy_filename, target_ou_id):

    # Read the SCP policy from the JSON file
    policy_file_path = os.path.join(policies_folder_path, policy_filename)
    with open(policy_file_path, 'r') as policy_file:
        policy_content = json.load(policy_file)

    # Create the SCP policy
    response = client.create_policy(
        Content=json.dumps(policy_content),
        Description=f'Policy from {policy_filename}',
        Name=policy_filename.split('.')[0],
        Type='SERVICE_CONTROL_POLICY'
    )
    # Extract the Policy ID from the response
    policy_id = response['Policy']['PolicySummary']['Id']
   
    # Attach the SCP policy to the target OU
    client.attach_policy(
        PolicyId=policy_id,
        TargetId=target_ou_id
    )
    print(f"Policy {policy_id} has been created and attached to OU {target_ou_id}.")

# Create and attach policies to the root OU
for policy_file in root_policies:
    create_and_attach_policy(policy_file, root_ou_id)

# Create and attach policies to the child OU
for policy_file in compliant_policies:
    create_and_attach_policy(policy_file, compliant_ou_id)