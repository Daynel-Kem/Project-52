import Image from 'next/image'
import React from 'react'
import { assets } from '../../../assets/assets'
import TextLoop from 'react-text-loop'

// I copied this Header from a Tutorial, but I REALLY DONT LIKE HOW IT LOOKS. It just feels super weak and unimposing

const Header = () => {
  return (
    <div className='w-11/12 max-w-3xl text-center mx-auto h-screen flex flex-col items-center justify-center gap-4'>
      <div>
        <Image src={assets.profile_img} alt="" className="rounded-full w-32"/>
      </div>
      <h3 className="flex items-end gap-2 text-xl md:text-2xl mb-3 Ovo">Hey, I'm Daniel Kim <Image src={assets.hand_icon} alt="" className="rounded-full w-6"/></h3>
      <div className="flex flex-col items-center text-left">
        <h1 className='text-3xl sm:text-6xl lg:text-[66px] Ovo'>
            I'm a          
            <TextLoop springConfig={{stiffness: 180, damping: 20}} className='ml-4 -z-10'>
            <h1 className='text-3xl sm:text-6xl lg:text-[66px] Ovo text-amber-400'> Student</h1>
            <h1 className='text-3xl sm:text-6xl lg:text-[66px] Ovo text-blue-700'> Developer</h1>
            <h1 className='text-3xl sm:text-6xl lg:text-[66px] Ovo text-red-800'> Friend</h1>
            </TextLoop> 
        </h1>

      </div>
      <p className='max-w-2xl mx-auto Ovo'>
        Whats up Lorem ipsum dolor sit amet consectetur adipisicing elit. Vel quod, facilis sit expedita iste quos doloribus labore, a perferendis voluptate, adipisci ad vitae harum? Iste nesciunt labore facilis consequatur illo.
      </p>
      <div className='flex flex-col sm:flex-row items-center gap-4 mt-4'>
        <a href="#contact" className='px-10 py-3 border border-white rounded-full bg-black text-white flex items-center gap-2'>Contact Me <Image src={assets.right_arrow_white} alt="" className="w-4"/></a>
        <a href="/sample-resume.pdf" download className='px-10 py-3 border rounded-full border-gray-500 flex items-center gap-2'>My Resume <Image src={assets.download_icon} alt="" className="w-4"/></a>
      </div>
    </div>
  )
}

export default Header
