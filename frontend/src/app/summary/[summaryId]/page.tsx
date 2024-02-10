"use client";

type Props = {
    params: {
        summaryId: string;
    }
}

const Summary = ({params: { summaryId }}: Props) => {
    return <h1>{summaryId}</h1>;
}
 
export default Summary;