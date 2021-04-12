import sys

KLASS_LIST = {
    'operator1': 'Operator1',
    'operator2': 'Operator2'
}


if __name__ == '__main__':
    operator_name = sys.argv[1]
    mod = __import__(operator_name)
    klass = getattr(mod, KLASS_LIST[operator_name])
    obj = klass()
    print(obj.run())
