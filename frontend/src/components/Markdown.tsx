import React from 'react';
import styles from './Markdown.module.css';

import ReactMarkdown from 'react-markdown';

type Props = {
    markdown: string;
}

const Markdown = ({markdown}: Props) => {
    return (
        <ReactMarkdown>
            {markdown}
        </ReactMarkdown>
    )
}
 
export default Markdown;