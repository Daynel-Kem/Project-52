import Image from 'next/image'
import React from 'react'
import { assets } from '../../../assets/assets'
import { useState } from 'react'

const Contact = () => {
    const [result, setResult] = useState("")

    const onSubmit = async (event) => {
      event.preventDefault();
      setResult("Sending....");
      const formData = new FormData(event.target);
  
      formData.append("access_key", "c7ec8bd1-f933-4fd9-b958-2d8ba14b514d");
  
      const response = await fetch("https://api.web3forms.com/submit", {
        method: "POST",
        body: formData
      });
  
      const data = await response.json();
  
      if (data.success) {
        setResult("Form Submitted Successfully");
        event.target.reset();
      } else {
        console.log("Error", data);
        setResult(data.message);
      }
    };
  

  return (
    <div id="contact" className='w-full px-[12%] py-10 scroll-mt-20 bg-[url("/footer-bg-color.png")] bg-no-repeat bg-center bg-[length:90%_auto]'>
        <h4 className='text-center mb-2 text-lg Ovo'>Connect with Me</h4>
        <h2 className='text-center text-5xl Ovo'>Contact</h2>

        <p className='text-center max-w-2xl mx-auto mt-5 mb-12 Ovo'>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Unde nesciunt dolorem eos impedit, voluptatibus deleniti sequi minima, adipisci placeat quod ad ipsa at in repudiandae itaque libero, rem voluptates corporis.
        </p>

        <form onSubmit={onSubmit} className='max-w-2xl mx-auto'>
            <div className='grid grid-cols-1 sm:grid-cols-2 gap-6 mb-6 mt-10'>
                <input type="text" placeholder="Your Name" name="name" id="" required className='flex-1 p-3 outline-none border-[0.5px] border-gray-400 rounded-md bg-white'/>
                <input type="email" placeholder="Your Email" name="email" id="" required className='flex-1 p-3 outline-none border-[0.5px] border-gray-400 rounded-md bg-white'/>
            </div>
            <textarea name="message" id="" rows="6" placeholder='Your Message' className='w-full p-4 outline-none border-[0.5px] border-gray-400 rounded-md bg-white mb-6'></textarea>
            <button type='submit' className='py-3 px-8 w-max flex items-center justify-between gap-2 bg-black/80 text-white rounded-full mx-auto hover:bg-black duration-500'>
            Submit <Image src={assets.right_arrow_white} alt="" className='w-4'/>
            </button>
            <p className='mt-4'>{result}</p>
        </form>

    </div>
  )
}

export default Contact
