import { useState } from 'react';
import { FaTimes, FaPlusCircle } from "react-icons/fa";
import styles from './CreateModal.module.css';

type Props = {
    trigger: React.ReactNode;
}

const CreateModal = ({ trigger }: Props) => {
    const [isOpen, setIsOpen] = useState(false);
    const [title, setTitle] = useState('');
    const [file, setFile] = useState<File | null>(null);

    const toggleOpen = () => {
        setIsOpen(!isOpen);
    }

    const handleKeyPress = (e: React.KeyboardEvent<HTMLInputElement>) => {
        if (e.key === 'Enter') {
            e.preventDefault();
            console.log('Enter pressed');
        }
    }

    const handleTitleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setTitle(e.target.value);
    }

    const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setFile(e.target.files ? e.target.files[0] : null);
    }

    const submitForm = async (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
    
        if (!file) {
            console.error('No file selected');
            return;
        }
    
        const formData = new FormData();
        formData.append('title', title);
        formData.append('file', file);
    
        try {
            const response = await fetch('http://127.0.0.1:5000/summaries', { // replace '/api/endpoint' with your API endpoint
                method: 'POST',
                body: formData,
            });
    
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
    
            const data = await response.json();
            console.log(data);
    
            // reset form and close modal
            setTitle('');
            setFile(null);
            toggleOpen();
        } catch (error) {
            console.error('Error:', error);
        }
    };

    return (
        <>
            <div className="trigger" onClick={toggleOpen}>
                {trigger}
            </div>
            {isOpen &&
                <div className={`${styles.background} ${isOpen ? styles.visible : ""}`}>
                    <div className={styles.modal}>
                        <button className={styles['close-button']} onClick={toggleOpen}>
                            <FaTimes />
                        </button>
                        <form className={styles['create-form']} onSubmit={submitForm}>
                            <h2 className='mb-'>Create a new lecture summary</h2>
                            <div className={styles['form-group']}>
                                <label>Title</label>
                                <input className={styles['text-input']} type="text" id="title" onKeyDown={handleKeyPress} onChange={handleTitleChange}/>
                            </div>
                            <div className={styles['form-group']}>
                                <label>Upload VTT transcript file</label>
                                <input type="file" onChange={handleFileChange}/>
                            </div>
                            <button type="submit" className={styles['submit-button']}>Summarize</button>
                        </form>
                    </div>
                </div>
            }
        </>
    );
}

export default CreateModal;