import React from 'react'
import { assets, serviceData } from '../../../assets/assets'
import Image from 'next/image'

// Change up the Services to actually reflect what you do

const Services = () => {
  return (
    <div id="services" className='w-full px-[12%] py-10 scroll-mt-20 h-screen'>
      <h4 className='text-center mb-2 text-lg Ovo'>What I Do</h4>
        <h2 className='text-center text-5xl Ovo'>My Services</h2>

        <p className='text-center max-w-2xl mx-auto mt-5 mb-12 Ovo'>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Unde nesciunt dolorem eos impedit, voluptatibus deleniti sequi minima, adipisci placeat quod ad ipsa at in repudiandae itaque libero, rem voluptates corporis.
        </p>

        <div className='grid lg:grid-cols-4 my-10 gap-6 '>
            {serviceData.map(({icon, title, description, link}, index)=>(
                <div key={index} className='border-grey-400 rounded-xl border-[0.5px] p-6 cursor-pointer hover:bg-green-50 hover:-translate-y-1 duration-500 hover:shadow-2xl flex flex-col items-center gap-4'>
                    <Image src={icon} alt="" className='w-10'/> 
                    <h3 className='text-lg my-4 text-gray-700'>{title}</h3>
                    <p className='text-gray-600 text-sm leading-5'>
                        {description} 
                    </p>
                    <a href={link} className='flex items-center gap-2 mt-5 text-sm text-gray-500 hover:text-gray-800 duration-300'>
                        Learn More <Image src={assets.right_arrow} className='w-4' alt=''/>
                    </a>
                </div>
            ))}
        </div>

    </div>
  )
}

export default Services
