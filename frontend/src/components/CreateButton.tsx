"use client";

import styles from './CreateButton.module.css';

import { FaPlusCircle } from "react-icons/fa";

const CreateButton = () => {
    return (  
        <button className={styles['create-button']}>
            <FaPlusCircle />
        </button>
    );
}
 
export default CreateButton;