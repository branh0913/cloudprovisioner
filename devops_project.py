from aws_provision import define_resources, deploy_instance
import troposphere
import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Program to create a stack")
    parser.add_argument('-s', '--stack_name', help='Use stack_name')
    parser.add_argument('d', '--delete_stack', help='Delete existing stack')
    args = parser.parse_args()

    template = troposphere.Template()

    payload = define_resources.generate_template(template=template)

    if args.delete_stack and args.stack_name:
        print("These 2 options can't be used together")

    try:
        define_resources.write_template(payload=payload)
    except (IOError, GeneratorExit) as ioerror:
        print(ioerror)

    stack_req = deploy_instance.create_stack(template_file='dev_template.template', stack_name=args.stack_name)

    if args.delete_stack:
        del_stack_req = deploy_instance.delete_stack(args.stack_name)




