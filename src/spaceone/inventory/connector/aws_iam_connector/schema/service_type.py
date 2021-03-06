from spaceone.inventory.libs.schema.dynamic_field import TextDyField, SearchField, DateTimeDyField, ListDyField, \
    EnumDyField
from spaceone.inventory.libs.schema.resource import CloudServiceTypeResource, CloudServiceTypeResponse, \
    CloudServiceTypeMeta

# GROUP
cst_group = CloudServiceTypeResource()
cst_group.name = 'Group'
cst_group.provider = 'aws'
cst_group.group = 'IAM'
cst_group.labels = ['Security']
cst_group.tags = {
    'spaceone:icon': 'https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/cloud-services/aws/AWS-Identity-and-Access-Management_IAM.svg',
}

cst_group._metadata = CloudServiceTypeMeta.set_meta(
    fields=[
        TextDyField.data_source('Group Name', 'data.group_name'),
        TextDyField.data_source('Users', 'data.user_count'),
        DateTimeDyField.data_source('Creation Time', 'data.create_date'),
    ],
    search=[
        SearchField.set(name='Group Name', key='data.group_name'),
        SearchField.set(name='Group ARN', key='data.arn'),
        SearchField.set(name='User Name', key='data.users.user_name'),
        SearchField.set(name='Policy Name', key='data.attached_permission.policy_name'),
        SearchField.set(name='Creation Time', key='data.create_date', data_type='datetime'),
    ]
)

# USER
cst_user = CloudServiceTypeResource()
cst_user.name = 'User'
cst_user.provider = 'aws'
cst_user.group = 'IAM'
cst_user.labels = ['Security']
cst_user.is_primary = True
cst_user.tags = {
    'spaceone:icon': 'https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/cloud-services/aws/AWS-Identity-and-Access-Management_IAM.svg',
}

cst_user._metadata = CloudServiceTypeMeta.set_meta(
    fields=[
        TextDyField.data_source('User Name', 'data.user_name'),
        ListDyField.data_source('Groups', 'data.groups', default_badge={
            'type': 'outline',
            'sub_key': 'group_name',
        }),
        TextDyField.data_source('Access Key Age', 'data.access_key_age_display'),
        TextDyField.data_source('Last Activity', 'data.last_activity'),
        EnumDyField.data_source('MFA', 'data.mfa_device', default_badge={
            'indigo.500': ['Virtual'], 'coral.600': ['Not enabled'],
        }),
    ],
    search=[
        SearchField.set(name='User Name', key='data.user_name'),
        SearchField.set(name='User ARN', key='data.arn'),
        SearchField.set(name='Group Name', key='data.user_name'),
        SearchField.set(name='Access Key Age', key='data.access_key_age', data_type='integer'),
        SearchField.set(name='Last Activity', key='data.last_active_age', data_type='integer'),
        SearchField.set(name='MFA', key='data.mfa_device'),
        SearchField.set(name='Policy Name', key='data.policies.policy_name'),
        SearchField.set(name='Access Key ID', key='data.access_key.key_id'),
        SearchField.set(name='Access Key Status', key='data.access_key.status', enums={
            'Active': {'label': 'Active'},
            'Inactive': {'label': 'Inactive'},
        }),
        SearchField.set(name='Access Key Created Time', key='data.access_key.create_date', data_type='datetime'),
        SearchField.set(name='Access Key Last Used', key='data.access_key.access_key_last_used.last_update_date',
                        data_type='datetime'),
        SearchField.set(name='SSH Key ID', key='data.ssh_public_key.key_id'),
        SearchField.set(name='SSH Key Status', key='data.ssh_public_key.status', enums={
            'Active': {'label': 'Active'},
            'Inactive': {'label': 'Inactive'},
        }),
        SearchField.set(name='SSH Key Upload Time', key='data.ssh_public_key.upload_date', data_type='datetime'),
        SearchField.set(name='CodeCommit User Name', key='data.code_commit_credential.service_user_name'),
        SearchField.set(name='CodeCommit Status', key='data.code_commit_credential.status', enums={
            'Active': {'label': 'Active'},
            'Inactive': {'label': 'Inactive'},
        }),
        SearchField.set(name='CodeCommit Created Time ', key='data.code_commit_credential.create_date',
                        data_type='datetime'),
        SearchField.set(name='Keyspaces User Name', key='data.cassandra_credential.service_user_name'),
        SearchField.set(name='Keyspaces Status', key='data.cassandra_credential.status', enums={
            'Active': {'label': 'Active'},
            'Inactive': {'label': 'Inactive'},
        }),
        SearchField.set(name='Keyspaces Created Time ', key='data.cassandra_credential.create_date',
                        data_type='datetime'),
        SearchField.set(name='Creation Time', key='data.create_date', data_type='datetime'),
    ]
)

# ROLE
cst_role = CloudServiceTypeResource()
cst_role.name = 'Role'
cst_role.provider = 'aws'
cst_role.group = 'IAM'
cst_role.labels = ['Security']
cst_role.tags = {
    'spaceone:icon': 'https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/cloud-services/aws/AWS-Identity-and-Access-Management_IAM.svg',
}

cst_role._metadata = CloudServiceTypeMeta.set_meta(
    fields=[
        TextDyField.data_source('Role Name', 'data.role_name'),
        ListDyField.data_source('Trusted Entities', 'data.trusted_entities', default_badge={'type': 'outline', 'delimiter': '<br>'}),
        TextDyField.data_source('Last Activity', 'data.last_activity'),
    ],
    search=[
        SearchField.set(name='Role Name', key='data.role_name'),
        SearchField.set(name='Role ARN', key='data.arn'),
        SearchField.set(name='Trust Relationships', key='data.trust_relationship.trust_relationship'),
        SearchField.set(name='Policy Name', key='data.policies.policy_name'),
        SearchField.set(name='Last Used Time', key='data.role_last_used.last_used_data', data_type='datetime'),
        SearchField.set(name='Creation Time', key='data.create_date', data_type='datetime'),

    ]
)

# POLICY
cst_policy = CloudServiceTypeResource()
cst_policy.name = 'Policy'
cst_policy.provider = 'aws'
cst_policy.group = 'IAM'
cst_policy.labels = ['Security']
cst_policy.tags = {
    'spaceone:icon': 'https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/cloud-services/aws/AWS-Identity-and-Access-Management_IAM.svg',
}

cst_policy._metadata = CloudServiceTypeMeta.set_meta(
    fields=[
        TextDyField.data_source('Policy Name', 'data.policy_name'),
        TextDyField.data_source('Policy ID', 'data.policy_id'),
        TextDyField.data_source('Attachment Count', 'data.attachment_count'),
    ],
    search=[
        SearchField.set(name='Policy Name', key='data.policy_name'),
        SearchField.set(name='Policy ARN', key='data.arn'),
        SearchField.set(name='Policy ID', key='data.policy_id'),
        SearchField.set(name='Permission Usage Count', key='data.permissions_boundary_usage_count',
                        data_type='integer'),
        SearchField.set(name='Update Time', key='data.update_date', data_type='datetime'),
        SearchField.set(name='Creation Time', key='data.create_date', data_type='datetime'),
        SearchField.set(name='Is Attachable', key='data.is_attachable', enums={
                    'true': {'label': 'true'},
                    'false': {'label': 'false'},
                }),
    ]
)

# IDENTITY PROVIDER
cst_identity_provider = CloudServiceTypeResource()
cst_identity_provider.name = 'IdentityProvider'
cst_identity_provider.provider = 'aws'
cst_identity_provider.group = 'IAM'
cst_identity_provider.labels = ['Security']
cst_identity_provider.tags = {
    'spaceone:icon': 'https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/cloud-services/aws/AWS-Identity-and-Access-Management_IAM.svg',
}

cst_identity_provider._metadata = CloudServiceTypeMeta.set_meta(
    fields=[
        TextDyField.data_source(name='Identity Provider URL', key='data.url'),
        EnumDyField.data_source(name='provider_type', key='data.provider_type', default_badge={'indigo.500': ['OIDC']}),
    ],
    search=[
        SearchField.set(name='Identity Provider URL', key='data.url'),
        SearchField.set(name='Identity Provider ARN', key='data.arn'),
        SearchField.set(name='Provider Type', key='data.provider_type'),
        SearchField.set(name='Creation Time', key='data.create_date', data_type='datetime')
    ]
)

CLOUD_SERVICE_TYPES = [
    CloudServiceTypeResponse({'resource': cst_group}),
    CloudServiceTypeResponse({'resource': cst_user}),
    CloudServiceTypeResponse({'resource': cst_role}),
    CloudServiceTypeResponse({'resource': cst_policy}),
    CloudServiceTypeResponse({'resource': cst_identity_provider}),
]
