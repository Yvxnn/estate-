{
    "name": "Real Estate Advertisement",
    "version": "1.0",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/estate_property_views.xml",
        "views/estate_property_type_views.xml",  # Ajoutez cette ligne
        "views/estate_menus.xml",
    ],
    "application": True,
}