from models import Organization

class OrganizationRequests(object):

    def organization_with_id(self, organization_id):
        return Organization.get(Organization.id == organization_id)

    def organization_with_name(self, name):
        return Organization.get(Organization.name == 'Cancer Awareness Organization')

    def organizations(self):
        organizations = []
        for organization in Organization.select():
            organizations.append(organization.dict())
        return organizations
