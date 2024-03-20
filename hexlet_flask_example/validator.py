def validate(post):
    errors = {}
    if not post.get('name'):
        errors['name'] = "Can't be blank"
    if not post.get('email'):
        errors['email'] = "Can't be blank"
    return errors