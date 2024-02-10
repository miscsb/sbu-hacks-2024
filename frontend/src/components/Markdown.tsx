import React from 'react';
import styles from './Markdown.module.css';

import ReactMarkdown from 'react-markdown';

import {Prism as SyntaxHighlighter} from 'react-syntax-highlighter';
import {duotoneDark} from 'react-syntax-highlighter/dist/cjs/styles/prism';

type Props = {
    markdown: string;
}

const Markdown = ({markdown}: Props) => {
    return (
        <ReactMarkdown 
            className={styles.markdown}
            components={{
                code(props) {
                  const {children, className, node, ...rest} = props
                  const match = /language-(\w+)/.exec(className || '')
                  return match ? (
                    <SyntaxHighlighter
                      {...rest}
                      PreTag="div"
                      language={match[1]}
                      style={duotoneDark}
                      className="rounded-lg"
                    >
                        {String(children).replace(/\n$/, '')}
                    </SyntaxHighlighter>
                  ) : (
                    <code {...rest} className={className}>
                      {children}
                    </code>
                  )
                }
            }}
        >
            {markdown}
        </ReactMarkdown>
    )
}
 
export default Markdown;