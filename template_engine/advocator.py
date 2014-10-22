from random import choice as c

issue_s1 = ['x', 'y', 'z']


def s1():   
    s1_1_w1 = ['I']
    s1_1_w2 = ['write', 'am writing', 'am concerned', 'have concerns', 'write you', 'am writing you', 'write to you', 'am writing to you']
    s1_1_w3 = ['about', 'concerning', 'regarding', 'with reference to', 'in regard to', 'with regard to']
    s1_1_w3_o1 = ['the matter of', 'the issue of', 'the question of', 'the problem of', 'the concern of', 'the topic of', 'this issue:', 'this matter:', 
                  'this question:', 'this problem:', 'this concern:', 'this topic:', 'the following issue:', 'the following matter:', 
                  'the following question:', 'the following problem:', 'the following concern:', 'the following topic:']
    s1_1_w4 = issue_s1
    s1_1_w5 = ['\b.']
    s1_1 = ' '.join([c(s1_1_w1), c(s1_1_w2), c(s1_1_w3), c(["\b", c(s1_1_w3_o1)]), c(s1_1_w4), c(s1_1_w5)])

    s1_2_w1 = ['This', 'My']
    s1_2_w2 = ['letter', 'note', 'message', 'request', 'inquiry', 'correspondence']
    s1_2_w3 = ['is about', 'concerns', 'is regarding', 'is in relation to', 'is in reference to']
    s1_2_w3_o1 = s1_1_w3_o1
    s1_2_w4 = issue_s1
    s1_2_w5 = ['\b.']
    s1_2 = ' '.join([c(s1_2_w1), c(s1_2_w2), c(s1_2_w3), c(["\b", c(s1_2_w3_o1)]), c(s1_2_w4), c(s1_2_w5)])

    s1_3_w1 = ['Please', 'I hope you will']
    s1_3_w2 = ['ensure', 'make sure', 'be certain', 'take heed', 'make certain']
    s1_3_w3 = ['that']
    s1_3_w4 = issue_s1
    s1_3_w5 = ['gets', 'receives', 'has']
    s1_3_w6 = ['your']
    s1_3_w7 = ['full', 'complete', 'undivided', 'absolute']
    s1_3_w8 = ['attention', 'notice', 'consideration', 'recognition', 'awareness']
    s1_3_w9 = ['\b.']
    s1_3 = ' '.join([c(s1_3_w1), c(s1_3_w2), c(s1_3_w3), c(s1_3_w4), c(s1_3_w5), c(s1_3_w6), c(s1_3_w7), c(s1_3_w8), c(s1_3_w9)])

    s1_4_w1 = ['I']
    s1_4_w2 = c([['\b'], ['strongly', 'firmly']])
    s1_4_w3 = ['urge', 'entreat', 'advise', 'recommend', 'implore', 'request', 'beseech', 'ask']
    s1_4_w4 = ['that you', 'you to']
    s1_4_w5 = s1_3_w2
    s1_4_w6 = ['that']
    s1_4_w7 = issue_s1
    s1_4_w8 = s1_3_w5
    s1_4_w9 = s1_3_w6
    s1_4_w10 = s1_3_w7
    s1_4_w11 = s1_3_w8
    s1_4_w12 = ['\b.']
    s1_4 = ' '.join([c(s1_4_w1), c(s1_4_w2), c(s1_4_w3), c(s1_4_w4), c(s1_4_w5), c(s1_4_w6), c(s1_4_w7), 
                     c(s1_4_w8), c(s1_4_w9), c(s1_4_w10), c(s1_4_w11), c(s1_4_w12)])

    s1_5_w1 = ['The', 'This']
    s1_5_w2 = ['issue of', 'matter of', 'question of', 'concern of',]
    s1_5_w3 = issue_s1
    s1_5_w4 = ['deserves', 'merits', 'warrants', 'demands', 'should get', 'must receive', 'should receive', 'must get']
    s1_5_w5 = s1_3_w6
    s1_5_w6 = s1_3_w7
    s1_5_w7 = s1_3_w8
    s1_5_w8 = ['\b.']
    s1_5 = ' '.join([c(s1_5_w1), c(s1_5_w2), c(s1_5_w3), c(s1_5_w4), c(s1_5_w5), c(s1_5_w6), c(s1_5_w7), c(s1_5_w8)])
    
    sentence1 = c([s1_1, s1_2, s1_3, s1_4, s1_5])
    return sentence1


def s2():
    s2_1_w1 = ['I appreciate', 'Thank you for', 'I would be encouraged by']
    s2_1_w2 = c([['your'], ['your prompt', 'your courteous', 'your immediate', 'your timely']])
    s2_1_w3 = ['attention', 'notice', 'consideration', 'recognition', 'awareness', 'concern']
    s2_1_w4 = ['for', 'of', 'towards', 'toward', 'to']
    s2_1_w5 = ['this']
    s2_1_w6 = ['\b', 'important', 'critical', 'crucial', 'essential', 'far-reaching', 'serious', 'significant', 'urgent', 'meaningful', 'vital', 'pressing']
    s2_1_w7 = ['issue', 'matter', 'concern', 'question', 'problem', 'topic', 'message', 'correspondence', 'letter', 'note', 'request', 'inquiry']
    s2_1_w8 = ['\b.']
    s2_1 = ' '.join([c(s2_1_w1), c(s2_1_w2), c(s2_1_w3), c(s2_1_w4), c(s2_1_w5), c(s2_1_w6), c(s2_1_w7), c(s2_1_w8)])
    
    s2_2_w1 = c([['Your'], ['Your prompt', 'Your courteous', 'Your immediate', 'Your timely']])
    s2_2_w2 = s2_1_w3
    s2_2_w3 = s2_1_w4
    s2_2_w4 = s2_1_w5
    s2_2_w5 = s2_1_w6
    s2_2_w6 = s2_1_w7
    s2_2_w7 = ['is', 'continues to be', 'remains']
    s2_2_w8 = ['appreciated', 'welcome', 'acknowledged', 'laudatory', 'commendatory']
    s2_2_w9 = ['\b.']
    s2_2 = ' '.join([c(s2_2_w1), c(s2_2_w2), c(s2_2_w3), c(s2_2_w4), c(s2_2_w5), c(s2_2_w6), c(s2_2_w7), c(s2_2_w8), c(s2_2_w9)])
    
    sentence2 = c([s2_1, s2_2])
    return sentence2


    

for _ in range(10):
    print '\n'
    sentence1 = s1()
    print '\n'
    sentence2 = s2()
    print sentence1 + ' ' + sentence2