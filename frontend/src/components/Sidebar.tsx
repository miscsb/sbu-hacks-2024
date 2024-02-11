"use client";

import Link from 'next/link';
import styles from './Sidebar.module.css';

import { useParams } from 'next/navigation';
import CreateButton from './CreateButton';

const Sidebar = async () => {

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

    const res = await fetch('http://127.0.0.1:5000/summaries', {
        method: 'GET',
    });

    const summaries: Summary[] = await res.json();

   
    // const summaries = [
    //     {
    //         id: '1',
    //         title: "Test summary 1",
    //     },
    //     {
    //         id: '2',
    //         title: "Test summary 2",
    //     },
    //     {
    //         id: '3',
    //         title: "Test summary 3",
    //     },
    // ]

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