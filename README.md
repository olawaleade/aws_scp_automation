# cloud-organization-policy
A repository for managing policies of each Public Cloud with code

 
## To Run the AWS SCP on the Repo locally
 #### Reference
 https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
 
1. Clone the Repository to local machine
2. Install the dependencies
    - pip install boto3
    - pip install pytest pytest-json-report (for pytest testing)
3. Set all AWS credential that has permission on Organization SCP, also another credential as a user to validate the test
    - export AWS_PROFILE=admin (with permission to Organization SCP)
    - export AWS_PROFILE=user (for testing)

### Commands to use

1. To create and attach the policy to OU,  (note that for this, you have to set aws credential to admin)
  
  - Run this command in CLI
    ```
     python3 test/policy-setup.py 
    ```

2. To run tests and generate JSON report from pytest testing (note that for this, you have to set AWS Credential to the user credential used to verify testing)
  
  - Run this command
    ```
     pytest test/unit_test.py --json-report --json-report-file=report.json
    ```

3. To detach and delete policy from OU,  (note that for this, you have to set aws credential to admin)
  
  - Run the command
    ```  
      python3 test/remove_scp.py
    ```

- Note that **Config.ini** file is used to store configuration data for flexibiltiy.
