#
# Copyright (c) 2018, Daniel Bolgheroni. All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
# 
#   1. Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#
#   2. Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in
#      the documentation and/or other materials provided with the
#      distribution.
# 
# THIS SOFTWARE IS PROVIDED BY DANIEL BOLGHERONI ''AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL DANIEL BOLGHERONI OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import csv
import argparse

from collections import OrderedDict


class SplitBill:
    def open(self, files):
        for f in files:
            with open(f) as f:
                reader = csv.DictReader(f,
                        fieldnames=('who','what', 'cost',),
                        restkey='between')

                for row in reader:
                    yield row

    def calculate(self, csv):
        # follow the convention used by the csv module
        paid = OrderedDict(); received = OrderedDict(); lent = OrderedDict()

        for row in csv:
            who = row['who']
            cost = float(row['cost'])
            between = row['between']

            # paid
            received.setdefault(who, 0) # paid but didn't received
            paid[who] = paid.setdefault(who, 0) + cost

            # received
            bw = [p for p in between if p] # remove empty fields
            split = cost / len(bw)

            for p in bw:
                paid.setdefault(p, 0) # received but didn't paid
                received[p] = received.setdefault(p, 0) + split

        for p in paid.keys():
           lent[p] = paid[p] - received[p]

        return lent

    def format_stdout(self, lent):
        if not lent:
            print("no bills")
            return

        for p in lent.keys():
            print("{} \t {:.2f}".format(p, lent[p]))

    def format_csv(self, lent, filename):
        with open(filename, 'w') as f:
            writer = csv.DictWriter(f, fieldnames=('who', 'lent'))

            for p in lent.keys():
                writer.writerow({'who': p, 'lent': lent[p]})
