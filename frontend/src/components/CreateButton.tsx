"use client";

import styles from './CreateButton.module.css';
import CreateModal from './CreateModal';

import { useState } from 'react';

import { FaPlus } from "react-icons/fa";

const CreateButton = () => {

    return (  
        <CreateModal 
            trigger={
                <button className={styles['create-button']}>
                    <FaPlus />
                </button>
            }
        />
    );

}
 
export default CreateButton;