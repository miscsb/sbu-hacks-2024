import styles from './Navbar.module.css';

import CreateButton from './CreateButton';

import Link from 'next/link';

const Navbar = () => {

    return ( 
        <nav className={styles.navbar}>
            <div>
                <Link href="/">
                    <h3>Lecture Summarizer</h3>
                </Link>
            </div>
            <div>
                <CreateButton />
            </div>
        </nav>
    );

}
 
export default Navbar;