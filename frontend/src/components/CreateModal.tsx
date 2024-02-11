import { useState } from 'react';
import { FaTimes } from "react-icons/fa";
import styles from './CreateModal.module.css';

import Snackbar from '@mui/material/Snackbar';
import Modal from '@mui/material/Modal';
import Box from '@mui/material/Box';

import { useRouter } from 'next/navigation';

type Props = {
    trigger: React.ReactNode;
}

const CreateModal = ({ trigger }: Props) => {

    const router = useRouter();

    const [isOpen, setIsOpen] = useState(false);
    const [title, setTitle] = useState('');
    const [file, setFile] = useState<File | null>(null);
    const [isSnackbarOpen, setIsSnackbarOpen] = useState(false);

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

        // reset form and close modal
        setTitle('');
        setFile(null);
        toggleOpen();
        setIsSnackbarOpen(true);
    
        try {
            const response = await fetch('http://127.0.0.1:5000/summaries', { // replace '/api/endpoint' with your API endpoint
                method: 'POST',
                body: formData,
            });
    
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
    
            const newSummary = await response.json();

            router.push(`/summary/${newSummary.id}`);


        } catch (error) {
            console.error('Error:', error);
        }
    };

    const body = (
        <Box sx={{ 
            position: 'absolute', 
            top: '50%', 
            left: '50%', 
            transform: 'translate(-50%, -50%)', 
            bgcolor: 'background.paper', 
            boxShadow: 24, 
            p: 4 
        }}>
            <button className={styles['close-button']} onClick={toggleOpen}>
                <FaTimes />
            </button>
            <form className={styles['create-form']} onSubmit={submitForm}>
                <h2>Create a new lecture summary</h2>
                <div>
                    <div className={styles['form-group']}>
                        <label>Title</label>
                        <input className={styles['text-input']} type="text" id="title" onKeyDown={handleKeyPress} onChange={handleTitleChange}/>
                    </div>
                    <div className={styles['form-group']}>
                        <label>Upload VTT transcript file</label>
                        <input type="file" onChange={handleFileChange}/>
                    </div>
                </div>
                <button type="submit" className={styles['submit-button']}>Summarize</button>
            </form>
        </Box>
    );

    return (
        <>
            <div className="trigger" onClick={toggleOpen}>
                {trigger}
            </div>
            <Modal
                open={isOpen}
                onClose={toggleOpen}
                aria-labelledby="modal-modal-title"
                aria-describedby="modal-modal-description"
            >
                {body}
            </Modal>
            <Snackbar
                open={isSnackbarOpen}
                anchorOrigin={{ vertical: 'bottom', horizontal: 'right' }}
                autoHideDuration={5000}
                onClose={() => setIsSnackbarOpen(false)}
                message="Your summary is being written. You will be redirected upon completion"
            />
        </>
    );
}

export default CreateModal;