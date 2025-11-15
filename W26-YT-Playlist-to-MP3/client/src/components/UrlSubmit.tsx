/* eslint-disable @typescript-eslint/no-unused-vars */
import React, { use } from 'react'
import { useState } from 'react'
import styles from './UrlSubmit.module.css'

export default function UrlSubmit() {
  const backendRoute: string = "https://2p8z7ni4e5.execute-api.us-east-2.amazonaws.com/production"
  const [url, setUrl] = useState("");
  const [loading, setLoading] = useState(false); 

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);

    try {
      const response = await fetch(
        `${backendRoute}/download`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            url: url
          })
        }
      )

      if (!response.ok) {
        throw new Error(`HTTP error: ${response.status}`)
      }

      const blob = await response.blob();

      const downloadUrl = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = downloadUrl;
      a.download = "output.zip";
      document.body.appendChild(a);
      a.click();
      a.remove()
      window.URL.revokeObjectURL(downloadUrl)

    } catch (err) {
      console.error("Download failed:", err);
      alert("Failed to download ZIP. Check console for details.")
    } finally {
      setLoading(false)
    }
  }

  return (<>
      <form onSubmit={handleSubmit}>
      <input 
        type="url" 
        placeholder='URL' 
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        />
      <button 
        type="submit"
        disabled={loading || !url}
        className={`${loading ? "loading" : "click"}`}
        >{loading ? "Processing" : "Download ZIP"}</button>
    </form>

    {loading && (
      <div style={{marginTop: "20px"}}>
        <div className={styles.spinner}>
        </div>
        <p>Preparing your download...</p>
      </div>
    )}
  </>

  )
}
