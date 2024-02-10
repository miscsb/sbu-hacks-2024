async function fetchData(url: URL | string | undefined) {
    try {

        if (!url) {
            throw new Error('No URL provided');
        }

        const response = await fetch(url);

        if (!response.ok) {
            throw new Error('Bad response from server');
        }

        return response

    } catch (error) {
        console.error('Error fetching data:', error);
        throw error;
    }
}

export default fetchData;