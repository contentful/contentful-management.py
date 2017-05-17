Contentful Management API SDK
=============================

.. image:: https://travis-ci.org/contentful/contentful-management.py.svg?branch=master
    :target: https://travis-ci.org/contentful/contentful-management.py

`Contentful <https://www.contentful.com>`_ is a content management platform for web applications, mobile apps and connected devices.
It allows you to create, edit & manage content in the cloud and publish it anywhere via powerful API.
Contentful offers tools for managing editorial teams and enabling cooperation between organizations.

Installation
------------

Install Contentful Management from the Python Package Index::

    sudo pip install contentful_management

Usage
-----

Client
------

Create a client::

    import contentful_management

    client = contentful_management.Client('MANAGEMENT_API_TOKEN')

The api token can easily be created through the `management api documentation <https://www.contentful.com/developers/docs/references/authentication/#the-content-management-api>`_.

Spaces
------

Retrieving all spaces::

    spaces = client.spaces().all()

Retrieveing one space by ID::

    blog_space = client.spaces().find('blog_space_id')

Deleting a space::

    client.spaces().delete('blog_space_id')

    # or if you already fetched the space

    blog_space.delete()

Creating a new space::

    new_blog_space = client.spaces().create({'name': 'My Blog', 'default_locale': 'en-US'})
    # default_locale is optional

In the case your user belongs to multiple organizations, you're required to send an organization ID::

    new_blog_space = client.spaces().create({'name': 'My Blog', 'organization_id': 'my_org_id'})

Updating a space::

    blog_space.update({'name': 'Ye Olde Blog'})

    # or directly editing it's properties

    blog_space.name = 'Ye Olde Blog'
    blog_space.save()

Assets
------

Retrieving all assets on a space::

    assets = client.assets('my_space_id').all()

    # or if you already have a fetched space

    assets = space.assets().all()

Retrieving an asset by ID::

    asset = client.assets('my_space_id').find('asset_id')

    # or if you already have a fetched space

    asset = space.assets().find('asset_id')

Deleting an asset::

    client.assets('my_space_id').delete('asset_id')

    # or if you already have a fetched space

    space.assets().delete('asset_id')

    # or if you already fetched the asset

    asset.delete()

Creating an asset::

    file_attributes = {
        'fields': {
            'file': {
                'en-US': {
                    'fileName': 'file.png',
                    'contentType': 'image/png',
                    'upload': 'https://url.to/file.png'
                }
            }
        }
    }

    new_asset = client.assets('my_space_id').create(
        'new_asset_id',
        file_attributes
    )

    # or if you already have a fetched space

    new_asset = space.assets().create(
        'new_asset_id',
        file_attributes
    )

We also support Direct File Upload, this will be explained in the Uploads section.

Processing an asset::

    asset.process()

This will process the file for every available locale and provide you with a downloadable URL within Contentful.

Updating an asset::

    asset.update(other_file_attributes)

    # or directly editing it's properties

    asset.file['file_name'] = 'other_file.png'
    asset.save()

Deleting an asset::

    client.assets('my_space_id').delete('asset_id')

    # or if you already have a fetched space

    space.assets().delete('asset_id')

    # or if you already fetched the asset

    asset.delete()

Archiving and Unarchiving an asset::

    asset.archive()
    asset.unarchive()

Publishing or Unpublishing an asset::

    asset.publish()
    asset.unpublish()

Checking if an asset is published::

    asset.is_published()

Entries
-------

Retrieving all entries on a space::

    entries = client.entries('my_space_id').all()

    # or if you already have a fetched space

    entries = space.entries().all()

    # or if you already have a fetched content type

    entries_for_content_type = content_type.entries().all()

Retrieving an entry by ID::

    entry = client.entries('my_space_id').find('entry_id')

    # or if you already have a fetched space

    entry = space.entries().find('entry_id')

    # or if you already have a fetched content type

    entry = content_type.entries().find('entry_id')

Deleting an entry::

    client.entries('my_space_id').delete('entry_id')

    # or if you already have a fetched space

    space.entries().delete('entry_id')

    # or if you already fetched the entry

    entry.delete()

Creating an entry::

    entry_attributes = {
        'fields': {
            'title': {
                'en-US': 'My Awesome Post'
            },
            'body': {
                'en-US': 'Once upon a time...'
            }
        }
    }

    new_entry = client.entries('my_space_id').create(
        'new_entry_id',
        entry_attributes
    )

    # or if you already have a fetched space

    new_entry = space.entries().create(
        'new_entry_id',
        entry_attributes
    )

Updating an entry::

    entry.update(other_entry_attributes)

    # or directly updating it's properties

    entry.title = 'My Super Post'
    entry.save()

Deleting an entry::

    client.entries('my_space_id').delete('entry_id')

    # or if you already have a fetched space

    space.entries().delete('entry_id')

    # or if you already fetched the entry

    entry.delete()

Archiving and Unarchiving an entry::

    entry.archive()
    entry.unarchive()

Publishing or Unpublishing an entry::

    entry.publish()
    entry.unpublish()

Checking if an entry is published::

    entry.is_published()


**Note**:

    Entries created with *empty fields*, will not return those fields in the response.
    Therefore, if you want to explicitly set those fields to empty (``None``) you will need to make an extra request to fetch the Content Type and fill the missing fields.

Content Types
-------------

Retrieving all content types on a space::

    content_types = client.content_types('my_space_id').all()

    # or if you already have a fetched space

    content_types = space.content_types().all()

Retrieving a content type by ID::

    content_type = client.content_types('my_space_id').find('content_type_id')

    # or if you already have a fetched space

    content_type = space.content_types().find('content_type_id')

Deleting a content type::

    client.content_types('my_space_id').delete('content_type_id')

    # or if you already have a fetched space

    space.content_types().delete('content_type_id')

    # or if you already fetched the content type

    content_type.delete()

Creating a content type::

    content_type_attributes = {
        'name': 'Blog Post',
        'description': 'Blog Posts to be included in ...'
        'fields': [
            {
                'disabled': False,
                'id': 'title',
                'localized': True,
                'name': 'Title',
                'omitted': False,
                'required': True,
                'type': 'Symbol',
                'validations': [
                    {
                        'size': {'min': 3}
                    }
                ]
            },
            {
                'disabled': False,
                'id': 'body',
                'localized': True,
                'name': 'Body',
                'omitted': False,
                'required': True,
                'type': 'Text',
                'validations': []
            }
        ]
    }

    new_content_type = client.content_types('my_space_id').create(
        'new_ct_id',
        content_type_attributes
    )

    # or if you already have a fetched space

    new_content_type = space.content_types().create(
        'new_ct_id',
        content_type_attributes
    )

Updating a content type::

    content_type.update(other_content_type_attributes)

    # or directly updating it's properties

    content_type.name = 'Not Post'
    content_type.fields.append(
        contentful_management.ContentTypeField({
            'id': 'author',
            'name': 'Author',
            'type': 'Link',
            'linkType': 'Entry'
        })
    )
    content_type.save()

Deleting a content type::

    client.content_types('my_space_id').delete('content_type_id')

    # or if you already have a fetched space

    space.content_types().delete('content_type_id')

    # or if you already fetched the content type

    content_type.delete()

Publishing or Unpublishing a content type::

    content_type.publish()
    content_type.unpublish()

Checking if a content type is published::

    content_type.is_published()

Removing a field from a content type::

    fields = content_type.fields

    # keep all fields but the one with 'author' as id

    content_type.fields = [ f for f in fields if not f.id == 'author' ]
    content_type.save()

Validations:

    For information regarding available validations check the `reference documentation <https://www.contentful.com/developers/docs/references/content-management-api/#/reference/content-types/content-type>`_.

Locales
-------

Retrieving all locales on a space::

    locales = client.locales('my_space_id').all()

    # or if you already have a fetched space

    locales = space.locales().all()

Retrieveing one locale by ID::

    locale = client.locales('my_space_id').find('locale_id')

    # or if you already have a fetched space

    locale = space.locales().find('locale_id')

Deleting a locale::

    client.locales('my_space_id').delete('locale_id')

    # or if you already have a fetched space

    space.locales().delete('locale_id')

    # or if you already have fetched the locale

    locale.delete()

Creating a new locale::

    new_locale = client.locales('my_space_id').create({'name': 'Klingon', 'code': 'tlh'})

    # or if you already have a fetched space

    new_locale = space.locales().create({'name': 'Klingon', 'code': 'tlh'})

Updating a locale::

    locale.update({'name': 'Elvish'})

    # or directly editing it's properties

    locale.name = 'Elvish'
    locale.save()

Roles
-----

Retrieving all roles on a space::

    roles = client.roles('my_space_id').all()

    # or if you already have a fetched space

    roles = space.roles().all()

Retrieveing one role by ID::

    role = client.roles('my_space_id').find('role_id')

    # or if you already have a fetched space

    role = space.roles().find('role_id')

Deleting a role::

    client.roles('my_space_id').delete('role_id')

    # or if you already have a fetched space

    space.roles().delete('role_id')

    # or if you already have fetched the role

    role.delete()

Creating a new role::

    role_attributes = {
      'name': 'My Role',
      'description': 'foobar role',
      'permissions': {
        'ContentDelivery': 'all',
        'ContentModel': ['read'],
        'Settings': []
      },
      'policies': [
        {
          'effect': 'allow',
          'actions': 'all',
          'constraint': {
            'and': [
              {
                'equals': [
                  { 'doc': 'sys.type' },
                  'Entry'
                ]
              },
              {
                'equals': [
                  { 'doc': 'sys.type' },
                  'Asset'
                ]
              }
            ]
          }
        }
      ]
    }

    new_role = client.roles('my_space_id').create(role_attributes)

    # or if you already have a fetched space

    new_role = space.roles().create(role_attributes)

Updating a role::

    roles.update({'name': 'A different Role'})

    # or directly editing it's properties

    role.name = 'A different Role'
    role.save()

Webhooks
--------

Retrieving all webhooks on a space::

    webhook = client.webhooks('my_space_id').all()

    # or if you already have a fetched space

    webhook = space.webhooks().all()

Retrieveing one webhook by ID::

    webhook = client.webhooks('my_space_id').find('webhook_id')

    # or if you already have a fetched space

    webhook = space.webhooks().find('webhook_id')

Deleting a webhook::

    client.webhooks('my_space_id').delete('webhook_id')

    # or if you already have a fetched space

    space.webhooks().delete('webhook_id')

    # or if you already have fetched the webhook

    webhook.delete()

Creating a new webhook::

    webhook_attributes = {
        'name': 'My Webhook',
        'url': 'https://www.example.com',
        'httpBasicUsername': 'username',
        'httpBasicPassword': 'password'
    }

    new_webhook = client.webhooks('my_space_id').create(webhook_attributes)

    # or if you already have a fetched space

    new_webhook = space.webhooks().create(webhook_attributes)

Updating a webhook::

    webhook.update({'name': 'Other Webhook'})

    # or directly editing it's properties

    webhook.name = 'Other Webhook'
    webhook.save()

Editor Interfaces
-----------------

Retrieving the editor interfaces for a content type::

    editor_interface = client.editor_interfaces('my_space_id', 'my_content_type_id').find()

    # or if you already have a fetched content type

    editor_interface = content_type.locales().find()

Updating the editor interface::

    controls = [
        {
            'widgetId': 'singleLine',
            'fieldId': 'name',
            'settings': {}
        }
    ]

    editor_interface.update({'controls': controls})

    # or directly editing it's properties

    editor_interface.controls = controls
    editor_interface.save()

Snapshots
---------

Retrieving all snapshots for an entry::

    snapshots = client.snapshots('my_space_id', 'entry_id').all()

    # or if you already have a fetched entry

    snapshots = entry.snapshots().all()

Retrieveing one snapshot by ID::

    snapshot = client.snapshots('my_space_id', 'entry_id').find('snapshot_id')

    # or if you already have a fetched entry

    snapshot = entry.snapshots().find('snapshot_id')

API Keys
--------

Retrieving all API keys on a space::

    api_keys = client.api_keys('my_space_id').all()

    # or if you already have a fetched space

    api_keys = space.api_keys().all()

Retrieveing one API key by ID::

    api_key = client.api_keys('my_space_id').find('api_key_id')

    # or if you already have a fetched space

    api_key = space.api_keys().find('api_key_id')

Deleting an API key::

    client.api_keys('my_space_id').delete('api_key_id')

    # or if you already have a fetched space

    space.api_keys().delete('api_key_id')

    # or if you already have fetched the locale

    api_key.delete()

Creating a new API key::

    new_api_key = client.api_keys('my_space_id').create({'name': 'My API Key'})

    # or if you already have a fetched space

    new_api_key = space.api_keys().create({'name': 'My API Key'})

Updating an API key::

    api_key.update({'name': 'Their API Key'})

    # or directly editing it's properties

    api_key.name = 'Their API Key'
    api_key.save()

Uploads
-------

Retrieveing one upload by ID::

    upload = client.uploads('my_space_id').find('upload_id')

    # or if you already have a fetched space

    upload = space.uploads().find('upload_id')

Deleting a upload::

    client.uploads('my_space_id').delete('upload_id')

    # or if you already have a fetched space

    space.uploads().delete('upload_id')

    # or if you already have fetched the upload

    upload.delete()

Creating a new upload::

    # you can use either a file-like object or a path.
    # If you use a path, the SDK will open it, create the upload and
    # close the file afterwards.

    with open('path/to/my/file.txt', 'rb') as file:
        new_upload = client.uploads('my_space_id').create(file)

    # or if you already have a fetched space

    new_upload = space.uploads().create('path/to/file.txt')

Associating an upload with a new asset::

    # notice that the upload is converted to a link,
    # and the JSON representation is then sent.

    client.assets('my_space_id').create(
       'new_asset_id',
       {
         'fields': {
           'file': {
             'en-US': {
               'fileName': 'some_name.png',
               'contentType': 'image/png',
               'uploadFrom': upload.to_link().to_json()
             }
           }
         }
       }
     )

Client Configuration Options
----------------------------

``access_token``: API Access Token.

``api_url``: (optional) URL of the Contentful Target API, defaults to Management API.

``uploads_api_url``: (optional) URL of the Contentful Upload Target API, defaults to Upload API.

``api_version``: (optional) Target version of the Contentful API.

``default_locale``: (optional) Default Locale for your Spaces, defaults to 'en-US'.

``https``: (optional) Boolean determining wether to use https or http, defaults to True.

``authorization_as_header``: (optional) Boolean determining wether to send access_token through a header or via GET params, defaults to True.

``raw_mode``: (optional) Boolean determining wether to process the response or return it raw after each API call, defaults to True.

``gzip_encoded``: (optional) Boolean determining wether to accept gzip encoded results, defaults to True.

``raise_errors``: (optional) Boolean determining wether to raise an exception on requests that aren't successful, defaults to True.

``content_type_cache``: (optional) Boolean determining wether to store a Cache of the Content Types in order to properly coerce Entry fields, defaults to True.

``proxy_host``: (optional) URL for Proxy, defaults to None.

``proxy_port``: (optional) Port for Proxy, defaults to None.

``proxy_username``: (optional) Username for Proxy, defaults to None.

``proxy_password``: (optional) Password for Proxy, defaults to None.

``max_rate_limit_retries``: (optional) Maximum amount of retries after RateLimitError, defaults to 1.

``max_rate_limit_wait``: (optional) Timeout (in seconds) for waiting for retry after RateLimitError, defaults to 60.

``application_name``: (optional) User application name, defaults to None.

``application_version``: (optional) User application version, defaults to None.

``integration_name``: (optional) Integration name, defaults to None.

``integration_version``: (optional) Integration version, defaults to None.

Logging
-------

To use the logger, use the standard library ``logging`` module::

    import logging
    logging.basicConfig(level=logging.DEBUG)

    client.entries().all()
    # INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.contentful.com
    # DEBUG:requests.packages.urllib3.connectionpool:"GET /spaces/cfexampleapi/entries HTTP/1.1" 200 1994

License
-------

Copyright (c) 2017 Contentful GmbH. See `LICENSE <./LICENSE>`_ for further details.

Contributing
------------

Feel free to improve this tool by submitting a Pull Request.
