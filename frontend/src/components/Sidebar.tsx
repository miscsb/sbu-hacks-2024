"use client";

import Link from 'next/link';
import styles from './Sidebar.module.css';

import { useParams } from 'next/navigation';
import CreateButton from './CreateButton';

const Sidebar = () => {

    const params = useParams();

    let currentId = '';

    if ('summaryId' in params) {
        if (typeof params.summaryId === 'string') {
            currentId = params.summaryId;
        } else {
            currentId = params.summaryId[0];
        }
    }

    type Summary = {
        id: string;
        title: string;
    }

    // get all summaries

    // const res = await fetch('http://127.0.0.1:5000/summaries', {
    //     method: 'GET',
    // });

    // const summaries: Summary[] = await res.json();

    const summaries = [
        {
            id: '1',
            title: "Test summary 1",
        },
        {
            id: '2',
            title: "Test summary 2",
        },
        {
            id: '3',
            title: "Test summary 3",
        },
        {
            id: '4',
            title: "Test summary 4",
        },
        {
            id: '5',
            title: "Test summary 5",
        },
        {
            id: '6',
            title: "Test summary 6",
        },
        {
            id: '7',
            title: "Test summary 7",
        },
        {
            id: '8',
            title: "Test summary 8",
        },
        {
            id: '9',
            title: "Test summary 9",
        },
        {
            id: '10',
            title: "Test summary 10",
        },
        {
            id: '11',
            title: "Test summary 11",
        },
        {
            id: '12',
            title: "Test summary 12",
        },
        {
            id: '13',
            title: "Test summary 13",
        },
        {
            id: '14',
            title: "Test summary 14",
        },
        {
            id: '15',
            title: "Test summary 15",
        },
        {
            id: '16',
            title: "Test summary 16",
        },
        {
            id: '17',
            title: "Test summary 17",
        },
        {
            id: '18',
            title: "Test summary 18",
        },
        {
            id: '19',
            title: "Test summary 19",
        },
        {
            id: '20',
            title: "Test summary 20",
        },
    ]

    return ( 
        <div className={styles.sidebar}>
            <div className={styles.summaries}>
                {summaries.map((summary) => (
                    <Link key={summary.id} href={`/summary/${summary.id}`}>
                        <div 
                            className={`${styles.title} ${summary.id === currentId ? styles['active'] : ''}`}
                        >
                            {summary.title}
                        </div>
                    </Link>
                ))} 
            </div>  
        </div>
    );
}
 
export default Sidebar;