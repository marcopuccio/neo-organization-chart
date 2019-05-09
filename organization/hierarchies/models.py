import neomodel


class Organization(neomodel.StructuredNode):
    organization_id = neomodel.UniqueIdProperty()
    name = neomodel.StringProperty(required=True)
    divisions = neomodel.RelationshipFrom(
        'hierarchies.models.Division',
        'FOR_ORGANIZATION',
        cardinality=neomodel.ZeroOrMore,
    )


class Division(neomodel.StructuredNode):
    division_id = neomodel.UniqueIdProperty()
    name = neomodel.StringProperty(required=True)
    organization = neomodel.RelationshipTo(
        'hierarchies.models.Organization',
        'FOR_ORGANIZATION',
        cardinality=neomodel.One,
    )
    persons = neomodel.RelationshipFrom(
        'hierarchies.models.Person',
        'WORKS_IN',
        cardinality=neomodel.ZeroOrMore,
    )


class Person(neomodel.StructuredNode):
    person_id = neomodel.UniqueIdProperty()
    full_name = neomodel.StringProperty(required=True)
    division = neomodel.RelationshipFrom(
        'hierarchies.models.Division',
        'WORKS_IN',
        cardinality=neomodel.ZeroOrOne,
    )
    boss = neomodel.Relationship(
        'self',
        'REPORTS_TO',
        cardinality=neomodel.ZeroOrOne,
    )
