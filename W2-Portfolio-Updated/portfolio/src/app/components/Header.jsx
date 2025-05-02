import Image from 'next/image'
import React from 'react'
import { assets } from '../../../assets/assets'
import TextLoop from 'react-text-loop'
import {motion} from 'motion/react'

const Header = () => {
  return (
    <div className='w-full h-screen flex flex-row justify-center items-center gap-10 z-10' style={{backgroundImage: `url(${assets.bg_image.src})`, backgroundSize: 'cover', backgroundPosition: 'center'}}>
      <motion.div 
      className='flex flex-col items-left justify-center text-left w-[50%] ml-40'
      initial={{opacity:0, x:-100}}
      whileInView={{opacity:1, x:0}}
      transition={{duration: 0.8, type: 'spring', stiffness: 100}}>
        <h3 className="flex gap-2 text-xl md:text-2xl mb-3 Ovo text-center sm:text-left">Hey, I'm Daniel Kim 
          <motion.div initial={{scale:0}} whileInView={{scale:1}} transition={{duration: 0.8, type: 'spring', stiffness: 100}}>
            <Image src={assets.hand_icon} alt="" className="rounded-full w-6"/>
          </motion.div>
        </h3>
        <div className="flex flex-col justify-end sm:width-[80%]">
          <h1 className='text-5xl sm:text-6xl lg:text-[66px] Ovo text-center sm:text-left'>
              I'm a           
          </h1>
          <TextLoop springConfig={{stiffness: 180, damping: 20}} noWrap={false} className='text-6xl text-left'>
              <h1 className='sm:text-6xl lg:text-[90px] Ovo text-amber-400'> Student</h1>
              <h1 className='sm:text-6xl lg:text-[90px] Ovo text-green-300'> Developer</h1>
              <h1 className='sm:text-6xl lg:text-[90px] Ovo text-red-800'> Friend</h1>
          </TextLoop>
        </div>
        <div className='flex flex-col sm:flex-row items-center gap-4 mt-4'>
          <a href="#contact" className='text-center px-10 py-2 border border-white rounded-full bg-black text-white flex items-center gap-2'>Contact Me <Image src={assets.right_arrow_white} alt="" className="w-4"/></a>
          <a href="/Daniel_Kim_DS_Resume.pdf" download className='px-10 py-2 border rounded-full border-black flex items-center gap-2 bg-white'>My Resume <Image src={assets.download_icon} alt="" className="w-4"/></a>
        </div>
      </motion.div>
      <div className='flex flex-col items-center justify-center w-[50%] mr-0'>
        {/* <Image src={assets.profile_img} alt="" className="rounded-full h-[70%] w-[40%]"/> */}
      </div>
    </div>
  )
}

export default Header
