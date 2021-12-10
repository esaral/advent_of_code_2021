#!/usr/bin/python

with open("$FILE", 'r') as f:
    data = [a.strip() for a in f.readlines()]

sum = 0

for d in data:
    signals, outputs = d.split(' | ')
    signals = signals.split()
    outputs = outputs.split()

    code = {}

    while len(signals):
        for signal in signals[:]:
            try:
                # Find unique numbers
                if len(signal) == 3:
                    code[7] = signal
                elif len(signal) == 4:
                    code[4] = signal
                elif len(signal) == 2:
                    code[1] = signal
                elif len(signal) == 7:
                    code[8] = signal
                
                # Find 0, 6, 9
                elif len(signal) == 6:
                    if all([l in signal for l in code[4]]):
                        code[9] = signal
                    elif all([l in signal for l in code[7]]):
                        code[0] = signal
                    else:
                        code[6] = signal

                # Find 2, 3, 5
                elif len(signal) == 5:
                    if all([l in code[6] for l in signal]):
                        code[5] = signal
                    elif all([l in code[9] for l in signal]):
                        code[3] = signal
                    else:
                        code[2] = signal

                signals.remove(signal)
            except KeyError as e:
                continue

    inv_code = {''.join(sorted(v)): k for k, v in code.items()}

    result = ''
    for output in outputs:
        output = ''.join(sorted(output))
        if output in inv_code:
            result += str(inv_code[output])
    
    sum += int(result)

print(sum)
