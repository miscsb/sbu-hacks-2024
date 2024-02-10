import Markdown from "@/components/Markdown";

type Props = {
    params: {
        summaryId: string;
    }
}

const SummaryPage = async ({params: { summaryId }}: Props) => {

    type Summary = {
        id: string;
        title: string;
        text_content: string;
    }

    // const res = await fetch(`http://127.0.0.1:5000/summaries/${summaryId}`, {
    //     method: 'GET',
    // });

    // const summary: Summary = await res.json();
    const summary = {
        id: '1',
        title: "Test summary 1",
        text_content: "# hi\n- test",
    }

    return (
        <div>
            <h1 className="mb-8 text-4xl underline">{summary.title}</h1>
            <Markdown markdown={summary.text_content} />
        </div>
    );

}
 
export default SummaryPage;