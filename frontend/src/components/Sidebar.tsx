import styles from './Sidebar.module.css';

const Sidebar = () => {

    const titles = [
        "Test title 1",
        "Test title 2",
        "Test title 3",
        "Test title 4",
        "Test title 5",
        "Test title 6",
        "Test title 7",
        "Test title 8",
        "Test title 9",
        "Test title 10",
        "Test title 11",
        "Test title 12",
        "Test title 13",
        "Test title 14",
        "Test title 15",
        "Test title 16",
        "Test title 17",
        "Test title 18",
        "Test title 19",
        "Test title 20",
    ]

    return ( 
        <div className={styles.sidebar}>
            {titles.map((title, index) => (
                <div key={index} className={styles.title}>
                    {title}
                </div>
            ))}
        </div>
    );
}
 
export default Sidebar;