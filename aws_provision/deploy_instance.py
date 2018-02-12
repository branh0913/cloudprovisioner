from boto import cloudformation


def create_stack(template_file=None, stack_name=None):
    cf_ops = cloudformation.CloudFormationConnection()
    try:
        with open(template_file) as dev_template:
            cf_ops.create_stack(stack_name, template_body=dev_template.read())
    except (IOError, Exception) as e:
        print(e)
        return None


def delete_stack(stack_id=None):

    try:
        cf_ops = cloudformation.CloudFormationConnection()
        return cf_ops.delete_stack(stack_id)
    except (Exception) as cf_ex:  #Couldn't find CF specific errors
        print(cf_ex)
        return None




