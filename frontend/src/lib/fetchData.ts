async function fetchData(url: URL | string | undefined) {
    try {

        if (!url) {
            throw new Error('No URL provided');
        }

        const response = await fetch(url);

        // console.log(response)

        if (!response.ok) {
            throw new Error('Bad response from server');
        }

        // const data = await response.json();

        return response

    } catch (error) {
        console.error('Error fetching data:', error);
        throw error;
    }
}

export default fetchData;