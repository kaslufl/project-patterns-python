from project_patterns import Profile, SerializerFactory


def test_profile_serializer():
    profile = Profile(1, 'Lucas', 'Leal')
    assert SerializerFactory.serializer(profile, 'Json') == '{"id": 1, "name": "Lucas", "last_name": "Leal"}'
    assert SerializerFactory.serializer(profile, 'Xml') == '<profile id="1"><name>Lucas</name><last_name>Leal</last_name></profile>'
