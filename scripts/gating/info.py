import yaml
import subprocess


model = 'models/gate/cifarnet.yaml'
dataset = 'datasets/cifar10.yaml'
ckpt_base = 'l1/latest'
files = [
    #  ('10', 0.1),
    #  ('20', 0.2),
    #  ('30', 0.3),
    #  ('40', 0.4),
    #  ('50', 0.5),
    #  ('60', 0.6),
    #  ('70', 0.7),
    #  ('80', 0.8),
    #  ('90', 0.9),
    #  ('100', 1.0),
    ('6', 0.9),
    ('8', 0.9),
    ('10', 0.9),
]

cmd_base = './my {} {} system.info.plumbing=true'
cmd_base = cmd_base.format(model, dataset)
results = []
for f, d in files:
    print(f)
    cmd = '{} system.checkpoint.load={}{} _gate.density={} eval info'
    cmd = cmd.format(cmd_base, ckpt_base, f, d)
    subprocess.call(cmd, cwd='../..', shell=True)
    with open('../../info.yaml', 'r') as y:
        i = yaml.load(y)
    s = i['layers']['footer']
    a = i['accuracies']
    results.append((f, s['macs'], s['weights'], a['top1'], a['top5']))
    print(results)
