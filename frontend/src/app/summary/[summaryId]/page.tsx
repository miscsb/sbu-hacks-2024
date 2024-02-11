'use client'

import Markdown from "@/components/Markdown";
import { useSearchParams } from "next/navigation";

type Props = {
    params: {
        summaryId: string;
    },
    searchParams: URLSearchParams;
}

const SummaryPage = async ({params: { summaryId }}: Props) => {

    const searchParams = useSearchParams()

    type Summary = {
        id: string;
        title: string;
        text_content: string;
    }

    const res = await fetch(`http://127.0.0.1:5000/summaries/${summaryId}`, {
        method: 'GET',
    });

    const summary: Summary = await res.json();
    // const summary = {
    //     id: '1',
    //     title: "Test summary 1",
    //     text_content: "# hi\n- test",
    // }

    var bionic = searchParams.get('bionic') ?? "false";
    var bionicLink = 'http://127.0.0.1:3000/summaries/' + summaryId + '?bionic=true';

    const makeBionic = () => {
        var separator = (window.location.href.indexOf("?")===-1)?"?":"&";
        window.location.href = window.location.href + separator + "bionic=true";
    }

    return (
        <div>
            <h1 className="mb-8 text-4xl underline">{summary.title}</h1>
            <Markdown markdown={make_bionic_content(summary.text_content)} />
            <Markdown markdown={summary.text_content} />
        </div>
    );

}

const is_word = (word : string) => {
    var match = word.match('^[a-zA-Z]+[.?!()]?$')
    return match != null && match.length > 0;
}

const make_bionic_word = (word : string) => {
    if (word.length <= 1) return word
    var mid = word.length / 2;
    return '**' + word.substring(0, mid) + '**' + word.substring(mid);
}

const make_bionic_line = (line : string) => {
    if (line.startsWith('#')) {
        return line;
    } else {
        var items = line.split(' ');
        items = items.map((item) => is_word(item) ? make_bionic_word(item) : item);
        return items.join(' ');
    }
}
    
const make_bionic_content = (text : string) => {
    var lines = text.split('\n');
    lines = lines.map(make_bionic_line);
    return lines.join('\n');
}
 
export default SummaryPage;