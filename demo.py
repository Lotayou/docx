import os
from docx import DocxFile
from argparse import ArgumentParser
import jieba
from jieba.analyse import extract_tags, textrank
import re

current_dir = os.path.dirname(os.path.realpath(__file__))

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-f', '--filename', type=str, 
        default=os.path.join(current_dir, 'work_log.docx'))
    parser.add_argument('-p', '--parse_output', type=str, 
        default='parse_result.txt')
    parser.add_argument('-a', '--analysis_output', type=str, 
        default='analysis_result.txt')
    parser.add_argument('--topK', type=int, default=30)
    args = parser.parse_args()

    x = DocxFile(args.filename)
    x.expandDocxFile()
    text_list = x.readdocx()
    
    with open(args.parse_output, 'w') as f:
        for line in text_list:
            if line is None:
                continue
            
            line_seg = [
                word for word in jieba.cut(line)
                if re.search(u'[\u4e00-\u9fff]', word)
            ]
            # strip non-Chinese words.
            f.write('|'.join(line_seg) + '\n')
                
    content = open(args.parse_output, 'r').read()
    tfidf_analysis_result = extract_tags(content, topK=args.topK, withWeight=True)
    trank_analysis_result = textrank(content, topK=args.topK, withWeight=True)
    
    with open(os.path.join(current_dir,
        'tfidf_' + args.analysis_output), 'w') as f:
        for word, freq in tfidf_analysis_result:
            f.write('{} {:10.4f}\n'.format(word, freq))
            
    with open(os.path.join(current_dir,
        'textrank_' + args.analysis_output), 'w') as f:
        for word, freq in trank_analysis_result:
            f.write('{} {:10.4f}\n'.format(word, freq))
    